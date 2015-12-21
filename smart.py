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
import sys
import unittest as _UT

_L = LoggerFactory.get("core", __name__)

# Example smart sensor insert data {}

################################################################################
# Module Globals
################################################################################
PROGRAM_VERSION = '0.0.1'
VERSION_START_DATE = '2015.12.20'
PROGRAM_NAME = 'Smart Command-line Interface (SmartCLI)'
PROGRAM_INFO = '{} v{} {} '.format(
	PROGRAM_NAME,
	PROGRAM_VERSION, 
	VERSION_START_DATE
	)
# Parser types
PT_BASE = 'base'
PT_SENSOR = 'sensor'
PT_INSERT_COMMAND = 'insert'
ARGS = None

################################################################################
# Events
################################################################################

################################################################################
# Module Classes
################################################################################

# Base parser and parser factory
class SmartCLIArgumentParser(argparse.ArgumentParser):
	def __init__(self, prog=None, usage=None, description=None):
		super(SmartCLIArgumentParser, self).__init__(
                        prog=PROGRAM_NAME,
                        usage=('Interact with the smart system from the '
                               'command-line to execute jobs, store data, '
                               'and more.'),
                        description=('Make sure to install, configure and '
                              'start a core controller and storage '
                              'node before using these commands.')
                        )

	def parse(self):
		'''Parse the arguments'''
		# TODO: Restrict arguments --> choices=[...]
		self.add_argument(
			PT_SENSOR,
			dest='perspective',
			type=list,
                        action='append',
                        nargs='+',
			help='Issue commands to the smart system acting as a sensor.'
                        #TODO: restrict options --> choices=[ 'insert', 'data' ]
                           	)
		self.add_argument(
			'version',
			type=bool,
			help='Print the version information.', #TODO
			action='version',
			version=PROGRAM_VERSION
				)
		args = 
		return self.parse_args()
		

class SmartArgumentParserFactory(object):
	@staticmethod
	def get(parser):
		'''Get a parser object.'''
		parser = parser.lower()
		if parser == PT_BASE:
			parser = SmartCLIArgumentParser()
		else:
			raise SmartCLIException()	
		return parser
		
class SmartSensorArgumentParser(argparse.ArgumentParser):
	def __init__(self, prog=None, usage=None, description=None):
		super(SensorArgumentParser, self).__init__()
	
	def parse(self):
		# TODO: Validate input
		self.add_argument(
			PT_INSERT_COMMAND,
			nargs=2,
			type=str,
			help='Insert a given json object or file' # TODO: File part --> Accept json or xml files, etc.. parse as json. -type flag?
                             #TODO: restrict options --> choices=[ 'insert', 'data' ]
			)

class SmartPerspectiveFactory(object):
	@staticmethod
	def get(perspective):
		'''Get the perspective parser'''
		perspective = perspective.lower()
		if perspective == PT_SENSOR:
			perspective = SmartSensorArgumentParser()
		else:
			raise SmartCLIException()
		return perspective

################################################################################
# Module Exceptions
################################################################################
class SmartCLIException(Exception):
	pass

################################################################################
# Module Functions
################################################################################
def process_arguments():
	'''Process the command-line arguments'''
	# TODO: refactor --> loop here?
	# Get perspective (i.e, 'sensor' perspective, etc)
	perspective = SmartArgumentParserFactory.get('base').parse()

	# Process command within perspective
	was_success = SmartPerspectiveFactory.get(perspective).parse()
	
	if not was_success:
		# TODO: If cmd fails, treat appropriately
		_L.error('command failed')
		raise NotImplementedError()
	
if __name__ == '__main__':
	process_arguments()

################################################################################
# Module Tests
###############################################################################
import subprocess

# TODO: Test each and every CLI command
class TestArgumentProcessing(_UT.TestCase):
	pass
