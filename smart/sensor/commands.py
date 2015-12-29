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

SUCCESS = "execution success: {}"
EXECUTING = "executing command: {}"
class SmartSystemCommand(commander.Command):
	def __init__(self, **kwargs):
		super(SmartSystemCommand, self).__init__()

class InsertSensorData(SmartSystemCommand):
	def __init__(self, **kwargs):
		super(InsertSensorData, self).__init__()
		validated_data = kwargs['data']
		assert(len(validated_data) > 2)
		assert( validated_data.get(G.UNIT_ID) != "")
		assert( validated_data.get(G.SENSOR_ID) != "")
		assert( len(validated_data.get(G.PAYLOAD)) > 0 )
		for key in G.STANDARD_DATA_KEYS:
			assert( key in validated_data )
		self._data = validated_data

	def invoke(self, **kwargs):
                '''Invoke the command. Calling this method signifies to the 
                   commander that that instance is ready for optimization
                   and execution'''
		LOG.info(EXECUTING.format(self.__class__.__name__))
		self.execute()
		LOG.info(SUCCESS.format(self.__class__.__name__))
		return self.execute()


	def execute(self, **kwargs):
		jdata = self.data()
		unit_id = jdata[G.UNIT_ID]
		sensor_id = jdata[G.SENSOR_ID]
		response = requests.post(
			"{}/{}/{}/{}/{}/".format(  REST_BASE, 
					G.REST_SENSORS,
					unit_id,
					sensor_id,
				 	G.REST_DATA ), 
			data=json.dumps(jdata)
		)
		if response.status_code != 200:
			LOG.error('error: status code: {}'.format(response.status_code))
			raise commander.CommandExecutionException()
		LOG.info('{} successful'.format(self.__class__.__name__))
		data = json.loads(response.text)
		data_id = data[G.PAYLOAD]
		LOG.info('network response : {}'.format(data))
		return { G.WAS_SUCCESS:True, G.PAYLOAD:data_id }

	def data(self):
		'''Get a deep copy of the data'''
		return copy.deepcopy(self._data)
