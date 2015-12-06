#
# Tests associated with module restful_service.py
#
import json as _JSON
import requests as _REQ
import unittest as _UT

from smart.core.system_logging import LoggerFactory as _LOG_FACTORY
import restful_service as _RS
################################################################################
# Globals
################################################################################
_BASE_RESOURCE_URL_FRAME = 'http://{}:{}'
_RESOURCE_BASE = _BASE_RESOURCE_URL_FRAME.format("127.0.0.1", "5000")
_LOG = _LOG_FACTORY.get("core", __name__).payload
_SAMPLE_SENSOR_DATA = {"key1":"value1", "key2":"value2", "key3":True}
_URL = _RESOURCE_BASE + "/sensors/sample_sensor_unit_id/sample_sensor_id/data/"

################################################################################
# Tests
################################################################################
class TestSensorToControllerInteractions(_UT.TestCase):

	def test_sensor_to_controller_data_storage_request(self):
		_REQUIRED_VALS = {
			"unsuccessful": { "error_occurred": self.verify_error_occurred, 
					  "raised_exception": self.verify_raised_exception, 
					  "raised_exception_message": 
						self.verify_exception_message
			 }, 
			"successful": { "payload": self.verify_payload }
		}

		# Post sample data to API
		response = _REQ.post(_URL, json=_SAMPLE_SENSOR_DATA)
		data_submit_response = response.json()
	
		# Process resulting json as necessary
		self.tests = None
		if not data_submit_response['was_success']:
			self.tests = _REQUIRED_VALS["unsuccessful"]
		else:
			self.tests = _REQUIRED_VALS["successful"]

			# Get posted sample date from API storage
			entry_id = data_submit_response['payload']
			response = _REQ.get(_URL + entry_id)
			data_request_response = response.json()

			if not data_request_response['was_success']:
                        	# TODO: Implement
				raise NotImplementedError() #TODO
                	else:
				sample_data = data_request_response['payload']
				
				# Clip data sample id if present
				if sample_data['_id'] is not None:
					del sample_data['_id']

				# Ensure originally posted sample data matches
				# that retrieved after closing the original
				# connection
				self.assertEqual( _SAMPLE_SENSOR_DATA, sample_data )

		# Verify each field
		for field,verification_function in self.tests.iteritems():
			self.assertIsNotNone(self.tests[field])
			self.assertTrue(verification_function(data_submit_response)) 
			#TODO: Make more specific. What should verification function
			#      really product? Etc? Develop better.

		# Run delete on submitted data to clean server

	def verify_error_occurred(self, *args):
		result = False
		dictionary = args[0]
		print dictionary #TODO
		self.assertFalse(dictionary["was_success"])
		self.assertIsNotNone(dictionary['error_occurred'])
		self.assertTrue(dictionary['error_occurred'])
		result = True
		return result
	
	def verify_raised_exception(self, *args):
		return True

	def verify_exception_message(self, *args):
		return True

	def verify_payload(self, *args):
		return True
