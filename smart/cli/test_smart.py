#
# Tests for the Smart CLI
#
# @author: Hayden McParlane
# @creation-date: 12.27.2015
import unittest as UT
import subprocess as SP
import requests as R
import datetime
import json as json

import smart.globals as G

################################################################################
# Globals
################################################################################
DT = datetime.datetime
CUR_DIR = "{}".format(G.SMART_SYSTEM_HOME)
MODULE_NAME = "{}/smart.py".format(CUR_DIR)

class TestSensorDataPerspective(UT.TestCase):
	def test_insert_sensor_data_cli_double_to_single_quote_formatted_data(self):
		command = [     'python',
                                MODULE_NAME,
                                G.REST_SENSOR,
                                'insert', 
                                'data',
                        r"{'test_key':'test_value'}" ]
		output = SP.check_output(command)
		was_success = False
		if "success" in output:
			was_success = True

		self.assertTrue(was_success)
	
	def test_insert_sensor_data_cli_single_to_double_quote_formatted_data(self):
		command = [ 	'python', 
				MODULE_NAME,
				G.REST_SENSOR, 
				'insert', 
				'data', 
			r'{"test_key":"test_value"}' ]
		output = SP.check_output(command)
		was_success = False
		if "success" in output:
			was_success = True
			
		self.assertTrue(was_success)

	def test_find_sensor_data_cli(self):
		command = [ 	'python',
				MODULE_NAME ]
		# smart sensor remove data id=A time=<time> ...
		# smart sensor find data id=<id> time=<time> ...
		# smart sensor update data id=<id> time=<time> ...
		# smart sensor insert data {}
		# smart sensor insert data id=A404823232 time=now this=that those=these

	def test_remove_sensor_data_cli(self):
		command = [  ]
		# smart sensor remove data id=
		# TODO
		

if __name__== "__main__":
	UT.main()