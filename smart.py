#!/usr/bin/python
################################################################################
# The command-line interface (CLI) into the smart system
#
# @author: Hayden McParlane
# @creation-date: 12.20.2015
################################################################################
import abc as _ABC
import argparse
import ast
import codecs as codecs
import collections
import json as json
from smart.core.system_logging import LoggerFactory
import smart.globals as G
import smart.sensor.commands as SC
import sys
# Example CLI use: smart sensor insert data {}
################################################################################
# Commands
################################################################################
TEST_UNIT_ID = 'test_unit_id'
TEST_SENSOR_ID = 'test_sensor_id'
OP_SUCCESS = 'success'
def insert_sensor_data(commands):
	'''Invoke the insert sensor data controller command.'''
	assert(isinstance(commands, list))
	assert(len(commands) > 3)
#	assert(isinstance(commands[3], dict))
	data = ast.literal_eval( commands[-1].encode('utf-8') )
	payload = dict()
	payload[G.PAYLOAD] = data
	payload[G.UNIT_ID] = TEST_UNIT_ID # TODO: FINISH
	payload[G.SENSOR_ID] = TEST_SENSOR_ID 
	# TODO: Ensure dict keys and values are as needed and aren't a
	#       security concern
	command = SC.InsertSensorData(data=payload)
	result = dict(invoke_command(command))
	print "{} {}".format(OP_SUCCESS, result[G.PAYLOAD])
        LOG.info(INVOKED.format(command.__class__.__name__))
	return result

def print_version(commands):
	print PROGRAM_INFO
################################################################################
# Functions
################################################################################
def construct_key(components):
	key = ':'.join(components)
	return key

INVOKED = '{} successfully invoked'
def invoke_command(command):
	'''Invoke a desired sensor command invoker.'''
#	assert(isinstance(command, smart.sensor.commands.SmartSystemCommand))
	result = command.invoke()
	LOG.info(INVOKED.format(command.__class__.__name__))
	return result

################################################################################
# Module Exceptions
################################################################################
class SmartCLIException(Exception):
	pass

################################################################################
# Globals
################################################################################
LOG = LoggerFactory.get("core", __name__).payload

# Setup module globals
PROGRAM_VERSION = '0.0.1'
VERSION_START_DATE = '12.20.2015'
PROGRAM_NAME = 'Smart Command-line Interface (SmartCLI)'
PROGRAM_INFO = '{}\nv{} {}\nCopywrite (c) 2015, {}'.format(
        PROGRAM_NAME,
        PROGRAM_VERSION,
        VERSION_START_DATE,
	"Hayden McParlane"
)

# Misc Commands
CMD_VERSION = 'version'

# System perspectives
CMD_SENSOR = 'sensor'

# System perspective commands
CMD_INSERT = 'insert'

# Sub Domain
CMD_DATA = 'data'

# Commands
INSERT_SENSOR_DATA = [CMD_SENSOR, CMD_INSERT, CMD_DATA]
PRINT_VERSION = [CMD_VERSION]

# Command Catalog
CC = {
        construct_key(INSERT_SENSOR_DATA) : insert_sensor_data,
	construct_key(PRINT_VERSION) : print_version
}

################################################################################
# Module Main
################################################################################
def process_arguments():
	'''Process the command-line arguments'''
	try:
		# TODO: refactor --> loop here?
		# Get perspective (i.e, 'sensor' perspective, etc)
		parser = argparse.ArgumentParser(
			prog=PROGRAM_INFO,
                        usage=('Interact with the smart system from the '
                               'command-line to execute jobs, store data, '
                               'and more.'),
                        description=('Make sure to install, configure and '
                              'start a core controller and storage '
                              'node before using these commands.')
		)
		parser.add_argument(
			'commands',
			type=str,
			action='store',
			nargs='+',
# TODO -->		choices=[],
			help='Interact with the smart system by entering commands.'
		)
		arguments = parser.parse_args()
		commands = arguments.commands
		# TODO: Validate input
		command = construct_key(
			commands[:] if len(commands) < 2 else commands[:-1]
		)
		was_success = False
		result = None
		if command in CC:
			# Get the command from the catalog and pass the terminal
			# commands as arguments to that command
			result = CC[command](commands[:])
			was_success = True
		if not was_success:
			# TODO: If cmd fails, treat appropriately
			LOG.error('command failed')
			raise NotImplementedError()
	except Exception, e:
		LOG.critical(e)
		sys.exit(1)
	
if __name__ == '__main__':
	process_arguments()
