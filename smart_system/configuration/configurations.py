
# Module used when programmatically configuring smart entity (Raspberry Pi, etc)
# 
# @author: Hayden McParlane
# @creation-date: 11.12.2015

import abc as _ABC
from smart_system.core import globals as _G
from smart_system.configuration import dependencies as _DEP

class Configuration(object):
	'''Abstract base class representing system component configuration. I.e, 
	controller storage configuration. After configuration, system will be 100%
	configured to be run.'''
	__metaclass__ = _ABC.ABCMeta
	def __init__(self, dependencies):
		'''Construct a configuration for the given OS type (i.e, linux)'''
		self.dependencies = dependencies
		assert(issubclass(self.dependencies(), DependencyCollectionInterface))
		assert(self.dependencies() is not None)

	def dependencies(self):
		'''Returns dictionary containing dependencies or None if none are 
		present. Dictionary returned contains install program as key and
		dependency as value. I.e, pip_installer=["pymongo", "requests"]'''
		return self.dependencies

