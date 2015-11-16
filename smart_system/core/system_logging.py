#!/usr/bin/python
# Application logging module
#
# @author: Hayden McParlane

import abc as _ABC
import colorlog as _COLORLOG
import logging as _L
import io
import smart_system.core.globals as _G
from signals import StatusSignal

###############################################################################
# Module constants
###############################################################################


_TEXT_FORMAT = (
	"{ 'log_level':'%(levelname)-9s', 'time_stamp':'%(asctime)-26s', "
	"'logger_name':'%(name)-12s', 'path_to_file':'%(pathname)s', "
	"'function_name':'%(funcName)s', 'line_number':'%(lineno)d', "
	"'message':'%(message)s' }"
		)

_TEXT_COLOR = '%(log_color)s'

_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p %Z'

_COLORED_FORMATTER = _COLORLOG.ColoredFormatter(
			_TEXT_COLOR + _TEXT_FORMAT,
			datefmt=_DATE_FORMAT,
			reset=True,
                        log_colors={
                                         'DEBUG'   : 'black',
                                         'INFO'    : 'green',
                                         'WARNING' : 'yellow',
                                         'ERROR'   : 'bold_red',
                                         'CRITICAL': 'bold_white,bg_red'
                                   },
                        secondary_log_colors={},
                        style='%'      )

_STANDARD_FORMATTER = _L.Formatter(_TEXT_FORMAT,datefmt=_DATE_FORMAT)
                        
###############################################################################
# Classes
###############################################################################
class LoggerFactory(object):
	@staticmethod
	def get(system_logging_type, desired_logger_name):
		'''Get a logger of the specified type.'''
		logger_obj = None
		was_success = False
		system_logging_type = system_logging_type.lower()
		if system_logging_type.lower() == "core":
			logger_obj = ColoredLogger(desired_logger_name).logger()
		else:
			raise ValueError()

		if logger_obj is not None:
			was_success = True
		return StatusSignal(was_success=was_success, payload=logger_obj)
		
			
class ColoredLogger(object):
	def __init__(self, module_name, level=_L.WARN):
		# . Initialize object to defaults
		self.logger("garbage_value")
		
		try:
			# . Create handler and set level to default
			file_handler = _L.FileHandler("{}.log".format(module_name))
			console_handler = _L.StreamHandler()
			
			file_handler.setLevel(level)
			console_handler.setLevel(level)

			# . Add formatter to handler
			file_handler.setFormatter(_STANDARD_FORMATTER)
			console_handler.setFormatter(_COLORED_FORMATTER)

			# . Get stream
			self.logger(_L.getLogger(module_name))

			# . Add handler to logger
			self.logger().addHandler(file_handler)
			self.logger().addHandler(console_handler)

			self.logger().info("Logger started")
		except Exception as e:
			print e
			exit(1)

	def logger(self, new_logger=None):
		if new_logger is not None:
			self._logger_obj = new_logger
		else:
			return self._logger_obj

def call_some_function(logger):
	logger.critical("OH NO!!!")

def main():
	logger = LoggerFactory.get("core", __name__).payload
	logger.debug("This is debug info.")
	logger.info("This is some info.")
	logger.warn("This is a warning.")
	logger.error("Some error occurred.")
	logger.critical("Some critical error occurred.")	

	call_some_function(logger)


if __name__ == '__main__':
	main()
