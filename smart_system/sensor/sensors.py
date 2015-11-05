#! /usr/bin/python
#
# The sensor object definitions for the smart system
# Author: Hayden McParlane
# Date: 11.4.2015

class Sensor(object):
	'''Abstract base class for all sensor types.'''
	def read(self):
		raise NotImplementedError()


