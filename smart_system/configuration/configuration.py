
# Module used when programmatically configuring smart entity (Raspberry Pi, etc)
# 
# @author: Hayden McParlane
# @creation-date: 11.12.2015

import abc as _ABC
from smart_system.core import globals as _G

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
