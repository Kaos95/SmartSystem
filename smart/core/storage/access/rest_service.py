#
# The sensor interface 
#
# @author: Hayden McParlane

from bson.objectid import ObjectId
from flask import Flask
import json as _JSON
app = Flask(__name__)

import pymongo as _PYMONGO
from flask import request
import requests as _R
from smart.core.system_logging import LoggerFactory as _LOG_FACTORY
from smart.core.signals import JsonStatusSignal
import sys
import time as _TIME
import unittest as _UNITTEST

# Initialize the logger
# TODO: Replace .payload syntax with appropriate signal-processor relationship
_LOG = _LOG_FACTORY.get("core", __name__).payload
_MONGO_CLIENT = _PYMONGO.MongoClient()
_DATA = 'data'

@app.route('/sensors/<sensor_unit_id>/<sensor_id>/data/', methods=['POST'])
def insert_sensor_data(sensor_unit_id, sensor_id):
	try:
		json_data = _JSON.loads(request.data)
		_LOG.debug("Inserting sensor data: {}".format(_JSON.dumps(json_data)))
		database = _MONGO_CLIENT[sensor_unit_id]
		collection = database[sensor_id]
		_LOG.debug("Inserting data into database. {}".format(_JSON.dumps(json_data)))
		ins_id = str(collection.insert_one(json_data).inserted_id)
		_LOG.debug("Insertion successful")
		return JsonStatusSignal(was_success=True, payload=ins_id).generate(), 200
	except Exception, e:
		#TODO: return a response with the appropriate status/error code, etc
		_LOG.warn("Exception occurred. Printing exception information.")
		_LOG.warn(e)
		return JsonStatusSignal(was_success=False, error_occurred=True).generate(), 500

@app.route('/sensors/<sensor_unit_id>/<sensor_id>/data/', methods=["GET"])
def retrieve_sensor_data(sensor_unit_id, sensor_id):
	try:
		database = _MONGO_CLIENT[sensor_unit_id]
		collection = database[sensor_id]
		_LOG.debug("Sampling data collection...")
		sample = collection.find_one()
		if sample['_id'] is not None:
			sample['_id'] = str(sample['_id'])
		return JsonStatusSignal(was_success=True, payload=sample).generate(), 201
	except Exception, e:
		_LOG.warn("Exception occurred. Printing exception information.")
		_LOG.warn(e)
		return JsonStatusSignal(was_success=False, error_occurred=True).generate(), 500

@app.route('/sensors/<sensor_unit_id>/<sensor_id>/data/<data_id>/', methods = ["GET"])
def get_specific_data_entry(self, sensor_unit_id, sensor_id, data_id):
	try:
		_LOG.debug("Fetching data item: {} | {} | {}".format(sensor_unit_id, sensor_id, data_id ))
		database = _MONGO_CLIENT[sensor_unit_id]
		collection = database[sensor_id]
		data = collection.find_one({'_id':ObjectId(data_id)})
		if data['_id'] is not None:
			data['_id'] = str(data['_id'])
		return JsonStatusSignal(was_success=True, payload=data).generate(), 200
	except Exception, e:
		_LOG.warn("Exception occurred. Printing exception information.")
                _LOG.warn(e)
                return JsonStatusSignal(was_success=False, error_occurred=True).generate(), 500

###############################################################################
# Testing
###############################################################################

_HOST = "127.0.0.1:5000"
_SUCCESS_STATUS = "was_success"
_CONTROLLER_HOST_ADDRESS = "http://{}/sensors/sample_sensor_unit_id/sample_sensor_id/data/"
_HOST_URL = _CONTROLLER_HOST_ADDRESS.format(_HOST)
_WAIT_TIME = 10

class TestPostDataFromSensorIntoSystemController(_UNITTEST.TestCase):
	def test_data_storage_retrieval(self):
		dataBefore = {"sample_key":"sample_data"}
		
		# 1. Post the data
		_REQ.post(_HOST_URL, data=dataBefore)
	
		_TIME.sleep(_WAIT_TIME)
		
		# 2. Retrieve the data
		response = _REQ.get(_HOST_URL)
		
		# 3. Check the contents for a match
		dataAfter = _JSON.loads(response.data)
		assertEqual(dataBefore, dataAfter)

class TestPostDataFromSensorIntoSystemControllerExceptionCatch(_UNITTEST.TestCase):
	def test_result_of_try_block_failure(self):
		pass

if __name__ == '__main__':
	app.run()
