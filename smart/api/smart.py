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
PROGRAM_NAME = 'Smart Command-line Interface (SmartCLI)'
PROGRAM_VERSION = '0.0.1'
VERSION_START_DATE = '2015.12.20'

################################################################################
# Module Classes
################################################################################
class SmartCLIArgumentParser(argparse.ArgumentParser):
	def __init__(self, prog=None, usage=None, description=None):
		super(SmartCLIArgumentParser, self).__init__(
								prog=prog, 
								usage=usage, 
								description=description
							    )

	def parse(self):
		'''Parse the arguments'''
		raise NotImplementedError()
		
	
class SensorArgumentParser(SmartCLIArgumentParser):
	def __init__(self, prog=None, usage=None, description=None):
		super(SensorArgumentParser, self).__init__()
	
	def parse(self, *args):	
		# TODO: Validate input
		command = args[0]
		

################################################################################
# Module Exceptions
################################################################################


################################################################################
# Module Functions
################################################################################
def process_arguments():
	'''Process the command-line arguments'''
	parser = SmartCLIArgumentParser(  prog=PROGRAM_NAME, 
					  usage=('Interact with the smart system from the '
					         'command-line to execute jobs, store data, '
					         'and more.'),
					  description=('Make sure to install, configure and '
						       'start a core controller and storage '
						       'node before using these commands.')
					)
	parser.add_argument( 'sensor', 
			     action='append_const', 
			     nargs='+', 
			     choices=[  ]
			   )
	arguments = parser.parse_args()
	

def main():
	process_arguments()

if __name__ == '__main__':
	main()

################################################################################
# Module Tests
###############################################################################
import subprocess
class TestArgumentProcessing(_UT.TestCase):
	
