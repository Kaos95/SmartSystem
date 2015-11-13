#
# Module used when programmatically configuring smart entity (Raspberry Pi, etc)
# 
# @author: Hayden McParlane
# @creation-date: 11.12.2015

import 

class Configuration(object):
	'''Abstract base class representing system component configuration. I.e, 
	controller storage configuration. After configuration, system will be 100%
	configured to be run.'''
	def __init__(self, os, dependencies):
		'''Construct a configuration for the given OS type (i.e, linux)'''
		self._OS = OSInterfaceFactory.get(os) 
		self._dependencies = dependencies
		assert(self.os() is not None)
		assert(self.dependencies() is not None)

	def apply(self):
		'''Apply the specified configuration on the current host system.
		WARNING: This will apply persistent modifications to the underlying 
		system.''' 
		
		# . Ensure system environment is setup
		self._setup_environment()

		# . Run configuration and installation

	def resolve_dependencies(self):
		'''Check to ensure dependencies are satisfied. If not, ensure they're
		met when function call finishes.'''
		if len(self.dependencies() or {}) is 0:
			return None
		else:
			for program, dependencies in self.dependencies().iteritems():
				self.get_os().
		
	def dependencies(self):
		'''Returns dictionary containing dependencies or None if none are 
		present. Dictionary returned contains install program as key and
		dependency as value. I.e, pip_installer=["pymongo", "requests"]'''
		return self.dependencies

	def os(self):
		'''Returns the current operating system interface object or None
		if none is present'''
		return self.os

class DependencyCollection(object):
	''' class for all dependency collections.'''	
	pass

class DependencyHashCollection(DependencyCollection):
	'''Collection that uses dictionary data stucture to employ hashing.'''
	

class OSInterfaceFactory(object):
	'''Factory used to generate operating system interfaces.'''
	@staticmethod
	def get(os_type):
		'''Returns operating system interface object corresponding to provided
		operating system type.'''
		if not issubclass(os_type.__class__, OSType):
			raise TypeError("os_type must be a child implementation of "
					"OSType() base class.")
		else:
			interface = None
			if 

class OSInterface(object):
	'''Abstract base class used for all operating system interfaces.'''
	pass

# TODO: Once more is understood about the specific requirements of sensor-based
# operating systems and specifics, this should be refined. Should it be OSInterface
# or hardware interface? What's the appropriate abstraction?
class LinuxInterface(OSInterface):
	'''Concrete OSInterface instance for use with linux'''

class OSTypeFactory(object):
	'''Factory for generating necessary operating system type objects.'''
	@staticmethod
	def get(os_type_str):
		'''Returns OSType instance.'''
		if os_type_str is None or len(os_type_str) is 0:
			return None
		else:
			os_obj = None
			if os_type_str.lowercase() is "linux":
				return
			

class OSType(object):
	'''Abstract base class representing operating system type 
	objects.'''
	pass

class LinuxType(OSType):
	'''Object representing linux operating system type.'''
	pass
