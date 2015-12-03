#
# Module containing all software signals relating to the system
# architecture.
#
# @author: Hayden McParlane
# @creation-date: 11.12.2015

import abc as _ABC

###############################################################################
# Signals
###############################################################################

class SignalInterface(object):
	'''Signal "interface"'''
	__metaclass__ = _ABC.ABCMeta

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

class JsonStatusSignal(RemoteSignal):
	'''Signal that represents response from RESTful API.'''
	def __init__(self):
		super(JsonStatusSignal, self).__init__()
	

###############################################################################
# Signal processors
###############################################################################

class SignalManager(object):
	'''An object which seamlessly processes signals.'''
	__metaclass__ == _ABC.ABCMeta
	pass

class StatusSignalManager(SignalManager):
	def __init__(self, ):
		super(StatusSignalManager, self).__init__()
	
