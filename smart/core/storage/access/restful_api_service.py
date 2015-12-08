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
import requests as _REQ
import os as _OS
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
		json_data = request.get_json()
		database = _MONGO_CLIENT[sensor_unit_id]
		collection = database[sensor_id]
		ins_id = str(collection.insert_one(json_data).inserted_id)
		return JsonStatusSignal(was_success=True, payload=ins_id).generate(), 200
	except Exception, e:
		#TODO: return a response with the appropriate status/error code, etc
		_LOG.warn(e)
		return JsonStatusSignal(was_success=False, error_occurred=True).generate(), 500

@app.route('/sensors/<sensor_unit_id>/<sensor_id>/data/', methods=["GET"])
def retrieve_sensor_data(sensor_unit_id, sensor_id):
	try:
		database = _MONGO_CLIENT[sensor_unit_id]
		collection = database[sensor_id]
		sample = collection.find_one()
		if sample['_id'] is not None:
			sample['_id'] = str(sample['_id'])
	except Exception, e:
		_LOG.warn(e)
		return JsonStatusSignal(was_success=False, error_occurred=True, ).generate(), 500

@app.route('/sensors/<sensor_unit_id>/<sensor_id>/data/<data_id>/', methods = ["GET"])
def get_sensor_data_entry(sensor_unit_id, sensor_id, data_id):
	try:
		database = _MONGO_CLIENT[sensor_unit_id]
		collection = database[sensor_id]
		data = collection.find_one({'_id':ObjectId(data_id)})
		if data['_id'] is not None:
			data['_id'] = str(data['_id'])
		return JsonStatusSignal(was_success=True, payload=data).generate(), 200
	except Exception, e:
                _LOG.warn(e)
                return JsonStatusSignal(was_success=False, error_occurred=True).generate(), 500

###############################################################################

_HOST = "127.0.0.1:5000"
_SUCCESS_STATUS = "was_success"
_CONTROLLER_HOST_ADDRESS = "http://{}/sensors/sample_sensor_unit_id/sample_sensor_id/data"
_HOST_URL = _CONTROLLER_HOST_ADDRESS.format(_HOST)
_WAIT_TIME = 10

class TestPostDataFromSensorIntoSystemController(_UNITTEST.TestCase):
	def test_data_storage_retrieval(self):
		sample_data = {"sample_key":"sample_value", "sample_key2":"sample_value2"}
		
		# 1. Post the data
		response1 =_REQ.post(_HOST_URL, data=sample_data)
		data = _JSON.loads(response1.text)
		sample_sensor_entry_id = None
		
		if data["was_success"] is None:
			raise IOError()		
		
		if not data["was_success"]:
			raise NotImplementedError() # TODO: What should be done here?
		else:
			sample_sensor_entry_id = data['payload']

			_TIME.sleep(_WAIT_TIME)
		
			# 2. Retrieve the data
			if sample_sensor_entry_id is not None:
				response2 = _REQ.get(_HOST_URL + "/" + 
					sample_sensor_entry_id)
				# 3. Check the contents for a match
				data2 = _JSON.loads(response2.text)
				self.assertEqual(sample_data, data2["payload"])

class TestPostDataFromSensorIntoSystemControllerExceptionCatch(_UNITTEST.TestCase):
	def test_result_of_try_block_failure(self):
		pass

if __name__ == '__main__':
	app.run()
