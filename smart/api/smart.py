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
import unittest as _UT

_L = LoggerFactory.get("core", __name__)

smart sensor insert data {}

################################################################################
# Module Globals
################################################################################
PROGRAM_VERSION = '0.0.1'
VERSION_START_DATE = '2015.12.20'
PROGRAM_INFO = 'Smart Command-line Interface (SmartCLI) v{} {} '.format(PROGRAM_VERSION,
                                                                        VERSION_START_DATE)

# Parser types
PT_BASE = 'base'
PT_SENSOR = 'sensor'
PT_INSERT_COMMAND = 'insert'
ARGS = None

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
		parser.add_argument(
			PT_SENSOR,
                        action='append',
                        nargs='+',
			help='Issue commands to the smart system acting as a sensor.',
			dest='perspective'
                        #TODO: restrict options --> choices=[ 'insert', 'data' ]
                           	)
		self.add_argument(
			'version',
			type=bool,
			help='Print the version information.' #TODO
			dest='version',
			action=( lambda x : print PROGRAM_INFO )
				)
		return self.parse_args()
		

class SmartArgumentParserFactory(object):
	@staticmethod
	def get(self, parser_type):
		'''Get a parser object.'''
		parser = None
		parser_type = parser_type.lower()
		if parser_type == PT_BASE:
			parser = SmartCLIArgumentParser()
		elif parser_type == PT_SENSOR:
			parser = SmartSensorArgumentParser()
		else:
			raise SmartCLIException()	
		return parser
		
# Secondary parsers	
class SmartSensorArgumentParser(argparse.ArgumentParser):
	def __init__(self, prog=None, usage=None, description=None):
		super(SensorArgumentParser, self).__init__()
	
	def parse(self, *args):
		# TODO: Validate input
		parser.add_argument(
			PT_INSERT_COMMAND,
			nargs=2,
			type=str,
			help='Insert a given json object or file' # TODO: File part --> Accept json or xml files, etc.. parse as json. -type flag?
                             #TODO: restrict options --> choices=[ 'insert', 'data' ]
			)

class CommandParser(argparse.ArgumentParser):
	def __init__(self, prog=None, usage=None, description=None):
		super(CommandParser, self).__init__(	
			prog=prog, 
			usage=usage, 
			description=description
			)
		
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
	# Run initial argument parse
	facade = SmartArgumentParserFactory.get('base').parse()

	# Get secondary parser and run secondary parse
	parser = SmartArgumentParserFactory.get(parser_type)
	facade.
	
	
	commands = parser.parse()

def add(key, argument):
	'''Add argument to module arguments'''
	ARGS[key] = argument

def main():
	process_arguments()

if __name__ == '__main__':
	main()

################################################################################
# Module Tests
###############################################################################
import subprocess
class TestArgumentProcessing(_UT.TestCase):
	# TODO
	def test_sensor_data_insert
	
