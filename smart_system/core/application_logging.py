#
# Application logging module
#
# @author: Hayden McParlane
# @creation-date:11.13.2015

from colorlog import ColoredFormatter
import logging
import smart_system.core.globals as _G

class SystemLogger(object):
	def __init__(self, log_file_name):
		self.formatter = ColoredFormatter( 
					'%(levelname)s : %(asctime)s : %(filename)s '
					'%(module)s %(funcName)s : %(lineno)d : %(message)s',
					datefmt='%m/%d/%Y %I:%M:%S %p',
					reset=True,
					log_colors={
							'DEBUG'   : 'cyan',
							'INFO'    : 'green',
							'WARNING' : 'yellow',
							'ERROR'   : 'red',
							'CRITICAL': 'red,bg_white'
						   },
					secondary_log_colors={},
					style='%'
						 )
		self.logger = logging.basicConfig(filename=filename, level=logging.DEBUG, 

def main():
	logging.basicConfig(filename="{}.log".format(_G.APP_NAME), level=logging.DEBUG, 
		format='%(levelname)s:%(asctime)s:%(filename)s:%(module)s:%(funcName)s:%(lineno)d:%(message)s')
	
	logging.info("Logger started")

if __name__ == '__main__':
	main()
