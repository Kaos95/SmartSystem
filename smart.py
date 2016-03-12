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
import re as re
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
	# TODO: Verify the security of use of literal_eval(...)
	data = ast.literal_eval( commands[-1].encode('utf-8') )
	print "***** TYPE : {} *****".format(data.__class__.__name__)
	payload = { 	G.PAYLOAD : data,
			G.UNIT_ID : TEST_UNIT_ID,
			G.SENSOR_ID : TEST_SENSOR_ID }
	# TODO: Ensure dict keys and values are as needed and aren't a
	#       security concern
	# TODO: ***** SCAN DATA TO ENSURE EVENTS AREN'T NEEDED *****
	rules = [ ThresholdRule(	60.0, 
					surpass=False, 
					data_key='temperature' ) ]
	scan(data, rules)
	command = SC.InsertSensorData(data=payload)
	response = dict(invoke_command(command))
	print "{} id={}".format(OP_SUCCESS, response[G.PAYLOAD])
        LOG.info(INVOKED.format(command.__class__.__name__))
	return response

def print_version(commands):
	print PROGRAM_INFO

################################################################################
# Rules (objects defining conditions under which event will be invoked)
################################################################################
# TODO: Look into execution efficiency of regular expressions in python.
#       Different way to do it? Should these be static methods?
class Rule(object):
	def is_satisfied(self, data):
		'''Check to see if the data satisfies the given rule. Return
		value is True is yes, False is no.'''
		raise NotImplementedError()

	def invoke_events(self):
		'''Invoke an attached event.'''
		raise NotImplementedError()

class SensorRule(Rule):
	def is_satisfied(self, data):
		pass

	def invoke_events(self):
		pass

class ThresholdRule(Rule):
	def __init__(self, threshold, surpass, events, data_key):
		'''Initialize the threshold rule with a threshold number and
		optional surpass value. surpass is used to specify whether
		the rule event should be invoked if the threshold is surpassed
		(surpass=True) or if dropped below (surpass=False).'''
		self.threshold = threshold
		self.surpass = surpass
		self.data_key = data_key
		self.events = events
		self.regex = "\\[\"\']{1}%s[\"\']{1}[ \t]*:{1}(.+?)\\"

	def is_satisfied(self, data):
		# This re finds the pattern that matches { ... "key": <value> ...}
		# and extracts the value from the string
		restr = self.regex % 
			(self.key)
		match = re.search(restr, data)
		print match
		# TODO: Implement using fewer comparisons and perhaps a different
		#       implementation all-together. Just for speed of dev now.
		if match:
			value = float(match.group(1))
			print value
			if surpass:
				if value <= self.threshold:
					pass
				else:
					self.invoke_events()
			else:
				if value >= self.threshold:
					pass
				else:
					self.invoke_events()
		else:
			raise ValueError()
			
			

	def invoke_events(self):
		for key, event in self.events.iteritems():
			event_name = self.event.__class__.__name__
			LOG.info(INVOKING.format(event_name))
			event.invoke()
			LOG.info(INVOKED.format(event_name))

################################################################################
# Functions
################################################################################
def construct_key(components):
	key = ':'.join(components)
	return key

def invoke_command(command):
	'''Invoke a desired sensor command invoker.'''
#	assert(isinstance(command, smart.sensor.commands.SmartSystemCommand))
	command_name = command.__class__.__name__
	LOG.info(INVOKING.format(command_name))
	result = command.invoke()
	LOG.info(INVOKED.format(command_name))
	return result

def scan(data, rules):
	'''Scan data for satisfaction of the passed rules.'''
	# TODO: Use threading to increase rule scan efficiency
	for rule in rules:
		if rule.is_satisfied(data):
			rule.invoke_events()


################################################################################
# Module Exceptions
################################################################################
class SmartCLIException(Exception):
	pass

################################################################################
# Globals
################################################################################
LOG = LoggerFactory.get("core", __name__).payload

# Standard module log messages
INVOKED = 'successfully invoked -> {}'
INVOKING = 'invoking -> {}'

# Setup module globals
PROGRAM_VERSION = '0.0.2'
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
CC = {	construct_key(INSERT_SENSOR_DATA) : insert_sensor_data,
	construct_key(PRINT_VERSION) : print_version }

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

		# TODO: Is this manner of key construction fool-proof? This may
		# result in logical errors later if the pattern below isn't
		# applicable to all situations (i.e, if 
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
