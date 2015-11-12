#!/usr/bin/python

#
# Script to setup environment dependencies for application.
# Changes:
#	
# @author: Hayden McParlane

import argparse

#
# Exceptions
#
class ENVException(Exception):
	pass

#
# Parse command line arguments
#
def parse_arguments():
	parser = argparse.ArgumentParser(description="Setup environment for application.")

	parser.add_argument('-m', '--mode', type=str, default=None, required=True,
		dest='mode', help='Choose running mode')

	args = parser.parse_args()

	if args.mode is None or len(args.mode) is 0:
		raise ENVException("Argument must be supplied")
	
	task = TaskFactory.get_task(args.mode)

	return task

class TaskFactory(object):
	@staticmethod
	def  get_task(argument):
		lowercase_arg = argument.lowercase()
		task = None
		if lowercase_arg is "setup":
			task = SetupEnvironment()
		elif lowercase_arg is "teardown":
			task = TeardownEnvironment()
		elif lowercase_arg is "restore":
			task = TeardownSetupEnvironment()
		else:
			raise ENVException("Argument not mappable to argument object.")

		return task

class Task(object):
	'''Abstract base class of all task objects'''
	_task_name = None
	def _set_task_name(self, name):
		self._task_name = name
	

class SetupEnvironment(Task):
	'''Setup environment task'''
	def __init__(self):
		super(SetupEnvironment, self).__init__()
		self._set_task_name("Environment Setup")


class TeardownEnvironment(Task):
	'''Teardown environment task'''
	def __init__(self):
		super(TeardownEnvironment, self).__init__()
		self._set_task_name("Environment Teardown")


class TeardownSetupEnvironment(Task):
	'''Perform teardown and subsequent setup of environment.'''
	def __init__(self):
		super(TeardownSetupEnvironment, self).__init__()
		self._set_task_name("Environment Restore")

def main():
	try:
		task = parse_arguments()

		# . Ensure user is sure about task:	
		if not isinstance(task, Task):
			raise ENVException("Invalid task encountered.")

		else:
			task.

	except Exception, e:
		raise Exception()

if __name__ == '__main__':
	main()
