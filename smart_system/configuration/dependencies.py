#
# Module containing all dependency objects
#
# @author: Hayden McParlane
# @creation-date: 11.12.2015

import abc as _ABC

class DependencyCollectionInterface(object):
        '''Interface for all dependency collections.'''
	__metaclass__ = _ABC.ABCMeta
	
	def __iter__(self):
		return self

	def next(self):
		# TODO: Finish the dependency collections.	

class DependencyHashCollection(DependencyCollectionInterface):
        '''Collection that uses dictionary data stucture to employ hashing.'''

