################################################################################
# The command-line interface (CLI) into the smart system
#
# @author: Hayden McParlane
# @creation-date: 12.20.2015
################################################################################
import abc as _ABC
import argparse
import collections
from smart.core.system_logging import LoggerFactory
from smart.perspectives import Perspective
import sys
import unittest as _UT

_L = LoggerFactory.get("core", __name__)

# Example CLI use: smart sensor insert data {}
################################################################################
# Actions (Commands)
################################################################################
INVOKED = 'command {} invoked'
class InsertSensorData(argparse.Action):
	'''Invoke insert sensor data'''
	def __call__(): #TODO: pass data param
		_L.info(INVOKED.format(class_name())

# Functions ####################################################################
def construct_key(*components):
	return ':'.join(*components)

def class_name(class_obj):
	return class_obj.__class__.__name__

################################################################################
# Module Classes
################################################################################
class SmartCLIPerspective(argparse.ArgumentParser):
	def __init__(self, prog=None, usage=None, description=None):
		super(SmartCLIPerspective, self).__init__(
                        prog=PROGRAM_INFO,
                        usage=('Interact with the smart system from the '
                               'command-line to execute jobs, store data, '
                               'and more.'),
                        description=('Make sure to install, configure and '
                              'start a core controller and storage '
                              'node before using these commands.')
                        )
		
	# Custom function for command parse and invokation
	def invoke(self, *command):
		'''Parse the arguments'''
		# TODO: Restrict arguments --> choices=[...]

		self.add_argument(
			PT_SENSOR,
			dest='perspective',
			type=list,
                        action='store',
                        nargs='+',
			help='Issue commands to the smart system acting as a sensor.'
                        #TODO: restrict options --> choices=[ 'insert', 'data' ]
                           	)
		self.add_argument(
			'version',
			dest='version',
			type=bool,
			action='version',
			help='Print version information.', #TODO
			version='%(prog)s'
				)

		arguments = self.parse_args()

		command_key = construct_key(*components)
		
class SmartPerspectiveFactory(object):
	@staticmethod
	def get(perspective):
		'''Get the perspective'''
		# TODO: Validate input
		perspective = perspective.lower()
		if perspective == PT_BASE:
                        perspective = SmartCLIPerspective()
		else:
			raise ValueError()
		return perspective

################################################################################
# Module Exceptions
################################################################################
class SmartCLIException(Exception):
	pass

################################################################################
# Module Main
################################################################################
def initialize():
	'''Initialize the module'''
	
	# Setup module globals
	PROGRAM_VERSION = '0.0.1'
	VERSION_START_DATE = '2015.12.20'
	PROGRAM_NAME = 'Smart Command-line Interface (SmartCLI)'
	PROGRAM_INFO = '{} v{} {} '.format(
	        PROGRAM_NAME,
        	PROGRAM_VERSION,
	        VERSION_START_DATE
        	)

	# Perspective types
	PT_BASE = 'base'

	# System perspectives
	PT_SENSOR = 'sensor'

	# System perspective commands
	PT_INSERT_COMMAND = 'insert'

	# Sub Domain
	SD_DATA = 'data'

	# Commands
	INSERT_SENSOR_DATA = [ PT_SENSOR, PT_INSERT_COMMAND, SD_DATA ]

	COMMANDS = {
        	INSERT_SENSOR_DATA : InsertSensorData
	}

	# Command catalog
	CC = { construct_key(*components) : command for command_components : command 
								in COMMANDS }	

def process_arguments():
	'''Process the command-line arguments'''
	try:
		# TODO: refactor --> loop here?
		# Get perspective (i.e, 'sensor' perspective, etc)
		perspective = SmartPerspectiveFactory.get('base').parse()
		

		# Process command
		if CC.contains_key():
		command = CC.incoke()
		was_success = SmartPerspectiveFactory.get(str(perspective[0]))
							.parse(perspective[1:])
	
		if not was_success:
			# TODO: If cmd fails, treat appropriately
			_L.error('command failed')
			raise NotImplementedError()
	except Exception, e:
		_L.critical(e)
		sys.exit(1)
	
if __name__ == '__main__':
	process_arguments()

################################################################################
# Module Tests
###############################################################################
import subprocess

# TODO: Test each and every CLI command
class TestArgumentProcessing(_UT.TestCase):
	pass
