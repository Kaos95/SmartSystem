#
# The sensor interface 
#

from flask import Flask
from flask_restful import Resource, Api
import json as _JSON
app = Flask(__name__)
api = Api(app)

import pymongo as PYMONGO
from flask import request
import requests as _R
from smart_system.core import system_logging as _SYSTEM_LOGGING
import time as _TIME

# Initialize the logger
# TODO: Replace .payload syntax with appropriate signal-processor relationship
_LOG = _SYSTEM_LOGGING.LoggerFactory.get("core", __name__).payload



_MONGO_CLIENT = PYMONGO.MongoClient()
_API = flask_restful.Api
_DATA = 'data'

@app.route('/sensors/<sensor_unit_id>/<sensor_id>/', methods=['GET', 'POST'])
def data(sensor_unit_id, sensor_id):
	sensordb = _MONGO_CLIENT[sensor_unit]
	json = None
	if request.method == 'POST':
		# . Extract data from request
		data = request.form[_DATA]
		json = {"reached":"POST", "sensor_unit":sensor_unit, "sensor_id":sensor_id}
		return json
	elif request.method == 'GET':
		#TODO
		raise NotImplementedError()

#
# Resource definitions
#
api.add_resource(SensorContext, '/sensors/')



###############################################################################
# Testing
###############################################################################

_HOST = "localhost:8080"
_SUCCESS_STATUS = "was_success"

class TestPostDataFromSensorIntoSystemController(TestCase):
	def test_run(self):
		response = _REQ.post("http://{}/sensors/".format(_HOST), data={"data-post-test"
			:"checking"})
	
		jsonPayload = _JSON.load(response.text)
		
		_TIME.sleep(10)
		
		
		
		
		
		


	def 

class Test

class TestToEnsureThatDataInsertionReturnsBooleanValue(TestCase):
	def setUp(self):
		
		
	def tearDown(self):
		

class TestToEnsureSSLAndTLSIsUsedForSecurityWithOauth(TestCase):
	def setUp(self):
		
	def tearDown(self):


if __name__ == '__main__':
	app.run()
