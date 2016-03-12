#
# Events module for smart system sensors
#
# @author: Hayden McParlane
# @creation-date: 1.1.2016
from pypatterns import commander as commander

class SensorEvent(commander.Command):
	def __init__(self, **kwargs):
		super(SensorEvent, self).__init__()


class TemperatureSensorThresholdExceedEvent(SensorEvent):
	def invoke(self, ):
		
	def execute(self, ):
		
