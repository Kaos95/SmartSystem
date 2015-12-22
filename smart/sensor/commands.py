#
# 
#
# @author: Hayden McParlane
# @creation-date: 12.22.2015
import pypatterns.commander as commander
import smart.logging

# TODO: The specific implementation connecting the sensor to the core of the
#       smart system doesn't need to be understood by the commands. Add an
#       object that will abstract away the specific "system-core-interface"
#       used so that it is flexible to change later on.
API = None
import

class SmartSystemCommand(commander.Command):
	'''Command to insert sensor data'''
	def invoke(**kwargs=None):
		# TODO: Use the REST API to store the JSON data
		
		commander.invoke( [self] )
