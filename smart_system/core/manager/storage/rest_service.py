#
# The sensor interface 
#
# @author: Hayden McParlane

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

@app.route('/sensors/data/', methods=['GET', 'POST'])
def data(sensor_unit_id, sensor_id):
	sensordb = _MONGO_CLIENT[sensor_unit_id]
	json = None
	if request.method == 'POST':
		# . Extract data from request
		data = request.form[_DATA]
		json = {"reached":"POST", "sensor_unit":sensor_unit_id, "sensor_id":sensor_id}
		return JsonStatusSignal()#TODO: Finish json status signal and re-write this portion
	elif request.method == 'GET':
		#TODO
		raise NotImplementedError()

###############################################################################
# Testing
###############################################################################

_HOST = "localhost:8080"
_SUCCESS_STATUS = "was_success"
_CONTROLLER_HOST_ADDRESS = "http://{}/sensors/data"
_HOST_URL = _CONTROLLER.format(_HOST)
_WAIT_TIME = 10

class TestPostDataFromSensorIntoSystemController(TestCase):
	def test_data_storage_retrieval(self):
		dataBefore = {"data_post_test":"did_it_post?"}
		
		# 1. Post the data
		_REQ.post(_HOST_URL, data=dataBefore)
	
		_TIME.sleep(_WAIT_TIME)
		
		# 2. Retrieve the data
		response = _REQ.get(_HOST_URL)
		
		# 3. Check the contents for a match
		dataAfter = response.text
		assertEqual(dataBefore, dataAfter)
		
	def test_feedback_provided_by_post_data_using_sensor_to_controller_rest_api(self):
		data={"testing_post_data_rest_responses":"how did things turn out?"}
		response =_REQ.post(_HOST_URL, data=data)
		jsonData = json.loads(response.text)
		for field in required_return_fields:
			if jsonData[field] is None:

class TestToEnsureThatDataInsertionReturnsBooleanValue(TestCase):
	def setUp(self):
		
		
	def tearDown(self):
		

class TestToEnsureSSLAndTLSIsUsedForSecurityWithOauth(TestCase):
	def setUp(self):
		
	def tearDown(self):


if __name__ == '__main__':
	app.run()
