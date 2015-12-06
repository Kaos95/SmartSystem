#
# Module containing all software signals relating to the system
# architecture.
#
# @author: Hayden McParlane
# @creation-date: 11.12.2015

import abc as _ABC
import json as _JSON

###############################################################################
# Signals
###############################################################################

class SignalInterface(object):
	'''Signal "interface"'''
	__metaclass__ = _ABC.ABCMeta
	pass

class StatusSignal(SignalInterface):
	'''Signal conveying system state.'''
	def __init__(self, was_success, payload=None):
		super(StatusSignal, self).__init__()
		self.was_successful = was_success
		self.payload = payload
		
SignalInterface.register(StatusSignal)	

class RemoteSignal(SignalInterface):
        '''Signal received from remote source (i.e, RESTful API, etc).'''
        __metaclass__ = _ABC.ABCMeta
        pass

SignalInterface.register(RemoteSignal)

_WAS_SUCCESS = "was_success"
_ERROR_OCCURRED = "error_occurred"
_PAYLOAD = "payload"
_ERRNO = "error_number"
_EXCP_MSG = "exception_message"

class JsonStatusSignal(RemoteSignal):
	'''Signal that represents response from RESTful API.'''
	def __init__(self, was_success=None, payload=None, error_occurred=None, raised_exception=None, raised_exception_message=None):
		super(JsonStatusSignal, self).__init__()
		self._json = {}
		self.process_status(was_success)
		self.process_error(error_occurred, raised_exception, raised_exception_message)
		self.process_payload(payload)

	def process_status(self, was_success=None):
		'''Process the status of the signal'''
		if was_success is None:
			return
		else:
			self.was_success(was_success)
			
	def process_error(self, error_occurred=None, errno=None, raised_exception=None, raised_exception_message=None):
		'''Process the error status of the signal'''
		if error_occurred is None:
			pass
		else:
			self.error_occurred(error_occurred)

		if errno is None:
			pass
		else:
			self.error_number(errno)

		if raised_exception is None:
			pass
		else:
			raise NotImplementedError()

		if raised_exception_message is None:
			pass
		else:
			self.exception_message(raised_exception_message)

	def process_payload(self, payload=None):
		'''Process the payload data of the signal'''
		if payload is None:
			return
		else:
			self.payload(payload)

	def was_success(self, new_val=None):
		'''Function to get or set the was_success value'''
		if new_val is None:
			return self.get_from_json(_WAS_SUCCESS) or None
		else:
			self.add_to_json(_WAS_SUCCESS, new_val)

	def error_occurred(self, new_val=None):
		'''Getter and setter for error_occurred field'''
		if new_val is None:
			return self.get_from_json(_ERROR_OCCURRED) or None
		else:
			self.add_to_json(_ERROR_OCCURRED, new_val)

	def error_number(self, new_val=None):
		'''Getter and setter for the json error number'''
		if new_val is None:
			return self.get_from_json(_ERRNO) or None
		else:
			self.add_to_json(_ERRNO, new_val)

	def exception_message(self, new_val=None):
		'''Getter and setter for the json exception message'''
		if new_val is None:
			return self.get_from_json(_EXCP_MSG) or None
		else:
			self.add_to_json(_EXCP_MSG, new_val)

	def payload(self, new_val=None):
		'''Getter and setter for the payload field'''
		if new_val is None:
			return self.get_from_json(_PAYLOAD) or None
		else:
			self.add_to_json(_PAYLOAD, new_val)

	def json(self, new_val=None):
		'''Getter and setter for json member var'''
		if new_val is None:
			return self._json
		else:
			self._json = new_val

	def generate(self):
		'''Generate associated signal'''
		return _JSON.dumps(self.json())

	def add_to_json(self, key, value):
		'''Add a key-value pair to the json object'''
		(self.json())[key] = value

	def get_from_json(self, key):
		'''Get the value associated with json key'''
		return (self.json())[key]

###############################################################################
# Signal processors
###############################################################################

class SignalManager(object):
	'''An object which seamlessly processes signals.'''
	__metaclass__ = _ABC.ABCMeta
	pass

class StatusSignalManager(SignalManager):
	def __init__(self, ):
		super(StatusSignalManager, self).__init__()
	
class SignalProcessor(object):
	pass

class JsonSignalProcessor(SignalProcessor):
	pass
