#
# The sensor interface 
#
# @author: Hayden McParlane

from bson.objectid import ObjectId
from flask import Flask
import json as json
app = Flask(__name__)

import pymongo as PYMONGO
from flask import request
import requests as _REQ
import os as _OS
from smart.core.system_logging import LoggerFactory as LOG_FACTORY
from smart.core.signals import JsonStatusSignal
import smart.globals as G
import sys
import time as _TIME
import unittest as _UNITTEST

# Initialize the logger
# TODO: Replace .payload syntax with appropriate signal-processor relationship
LOG = LOG_FACTORY.get("core", __name__).payload
MONGO_CLIENT = PYMONGO.MongoClient()

INSERTING_DATA = "inserting sensor data -> {}"
FETCHING_DATA = "fetching sensor data -> id {}"
SUCCESS = "{} successful"

@app.route("/{}/{}/{}/".format(G.REST_SENSORS, G.REST_SENSOR, G.REST_DATA), 
	methods=["POST"])
def insert_sensor_data_item():
	try:
		# TODO: Validate input -> If entries contain invalid characters (i.e,
		#       a key string containing a ':' or something)
		json_payload = json.loads(request.data)
		for key in G.STANDARD_DATA_KEYS:
			assert( key in json_payload )
		unit_id = json_payload.get(G.UNIT_ID)
		sensor_id = json_payload.get(G.SENSOR_ID)
		database = MONGO_CLIENT[ unit_id ]
		collection = database[ sensor_id ]
		data = json_payload[G.PAYLOAD]
		LOG.info(INSERTING_DATA.format(data))
		ins_id = str(collection.insert_one(data).inserted_id)
		LOG.info(SUCCESS.format("insert"))
		return JsonStatusSignal(was_success=True, payload=ins_id).generate(), 200
	except Exception, e:
		#TODO: return a response with the appropriate status/error code, etc
		LOG.error(e)
		return JsonStatusSignal(was_success=False, error_occurred=True).generate(), 500

@app.route("/{}/{}/{}/<data_id>".format(G.REST_SENSORS, G.REST_SENSOR, G.REST_DATA), 
	methods = ["GET"])
def read_sensor_data_item(data_id):
	try:
		json_payload = json.loads(request.data)
                for key in G.STANDARD_DATA_KEYS:
                        assert( key in json_payload )
		data_id = json_payload[G.PAYLOAD]
		unit_id = json_payload[G.UNIT_ID]
		sensor_id = json_payload[G.SENSOR_ID]
                database = MONGO_CLIENT[ unit_id ]
                collection = database[ sensor_id ]
		LOG.info(FETCHING_DATA.format(data_id))
		data = collection.find_one( {'_id':ObjectId( data_id )}	)
		LOG.info(SUCCESS.format("fetch"))
		if data['_id'] is not None:
			data['_id'] = str(data['_id'])
		return JsonStatusSignal(was_success=True, payload=data).generate(), 200
	except Exception, e:
                LOG.warn(e)
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
		data = json.loads(response1.text)
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
				data2 = json.loads(response2.text)
				self.assertEqual(sample_data, data2["payload"])

class TestPostDataFromSensorIntoSystemControllerExceptionCatch(_UNITTEST.TestCase):
	def test_result_of_try_block_failure(self):
		pass

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)
