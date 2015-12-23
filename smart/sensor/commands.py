#
# Sensor commands allowing interface with the smart system core. 
#
# @author: Hayden McParlane
# @creation-date: 12.22.2015
import json as json
from pypatterns import commander as commander
import requests
from smart.core.system_logging import LoggerFactory

# TODO: The specific implementation connecting the sensor to the core of the
#       smart system doesn't need to be understood by the commands. Add an
#       object that will abstract away the specific "system-core-interface"
#       used so that it is flexible to change later on.
API = None

REST_BASE = 'http://159.203.246.108:5000/sensors/sample_unit/sample_id'
LOG = LoggerFactory.get('core', __name__).payload

class InsertSensorData(commander.Command):
	def __init__(self, **kwargs):
		super(InsertSensorData, self).__init__()
		self.data = kwargs['data']
		print "IN smart.sensor.commands.InsertSensorData(...)"
		
	def execute(self, **kwargs):
		LOG.info('{} executing'.format(self.__class__.__name__))
		jdata = self.data
		print jdata
		response = requests.post(REST_BASE + '/data/', data=json.dumps(jdata))
		print response.text
		LOG.info('network response : {}'.format(response.text))
		if response.status_code != 200:
			LOG.error('error: Response status: {}'.format(response.status_code))
			raise commander.CommandExecutionException()
			return False # Is this necessary?
		LOG.info('{} successful'.format(self.__class__.__name__))
