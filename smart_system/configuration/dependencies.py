#
# Module containing all dependency objects
#
# @author: Hayden McParlane
# @creation-date: 11.12.2015

import abc as _ABC

class DependencyCollectionInterface(object):
        '''Interface for all dependency collections.'''
	__metaclass__ = _ABC.ABCMeta
	
	@_ABC.abstractmethod
	def __iter__(self):
		raise NotImplementedError()

	@_ABC.abstractmethod
	def next(self):
		raise NotImplementedError()

	@_ABC.abstractmethod
	# TODO: Add generic interface for collection access

class DependencyHashCollection(DependencyCollectionInterface):
        '''Collection that uses dictionary data stucture to employ hashing.'''
	def __init__(self, dependencies=None):
		assert(issubclass(dependencies, DependencyCollectionInterface)
			or dependencies is None)

		self.dependencies() = {}
	
	# TODO: Each dependency should be paired with the location from which
	# the dependency can be resolved.
	
	def __iter__(self):
		return self
	
	def next(self):
		'''Return next dependency in collection.'''
		return self.

	def dependencies(self):
		return self.dependencies()
	
DependencyCollectionInterface.register(DependencyHashCollection)

class DependencyInterface(object):
	'''Interface for all dependencies.'''
	__metaclass__ = _ABC.ABCMeta
	
	@_ABC.abstractmethod
	def resolve

class PipDependency(DependencyInterface):
	pass
