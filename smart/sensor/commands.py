#
# Sensor commands allowing interface with the smart system core. 
#
# @author: Hayden McParlane
# @creation-date: 12.22.2015
import copy
import json as json
from pypatterns import commander as commander
import requests
from smart.core.system_logging import LoggerFactory
import smart.globals as G

# TODO: The specific implementation connecting the sensor to the core of the
#       smart system doesn't need to be understood by the commands. Add an
#       object that will abstract away the specific "system-core-interface"
#       used so that it is flexible to change later on.
API = None

# TODO: Modify URL to be dynamic and to be pulled from the json data
REST_BASE = G.REST_BASE_STORAGE
LOG = LoggerFactory.get('core', __name__).payload

UNIT_ID = G.UNIT_ID
SENSOR_ID = G.SENSOR_ID
PAYLOAD = G.PAYLOAD

EXECUTING = "executing command: {}"
class SmartSystemCommand(commander.Command):
	def __init__(self, **kwargs):
		super(SmartSystemCommand, self).__init__()

class InsertSensorData(SmartSystemCommand):
	def __init__(self, **kwargs):
		super(InsertSensorData, self).__init__()
		validated_data = kwargs['data']
		assert(isinstance(validated_data, dict))
		assert(len(validated_data) > 2)
		assert( validated_data.get(UNIT_ID) != "")
		assert( validated_data.get(SENSOR_ID) != "")
		assert( isinstance(validated_data.get(PAYLOAD), dict))
		assert( len(validated_data.get(PAYLOAD)) > 0 )
		for key in G.STANDARD_DATA_KEYS:
			assert( key in validated_data )
		self._data = validated_data

	def execute(self, **kwargs):
		LOG.info(EXECUTING.format(self.__class__.__name__))
		jdata = self.data()
		print jdata
		response = requests.post(
			"{}/{}/{}/{}/".format(  REST_BASE, 
					G.REST_SENSORS, 
					G.REST_SENSOR,
				 	G.REST_DATA ), 
			json=json.dumps(jdata)
		)
		print response.text
		LOG.info('network response : {}'.format(response.text))
		if response.status_code != 200:
			LOG.error('error: Response status: {}'.format(response.status_code))
			raise commander.CommandExecutionException()
			return False # Is this necessary?
		LOG.info('{} successful'.format(self.__class__.__name__))

	def data(self):
		'''Get a deep copy of the data'''
		return copy.deepcopy(self._data)
