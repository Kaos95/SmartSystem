################################################################################
# Controller Commands
#
# @author: Hayden McParlane
# @creation-date: 12.21.2015
################################################################################
import argparse
import pypatterns.commander as commander

class InsertSensorData(commander.Command):
        '''Insert a sensors data into smart system core'''
        def __init__(self, data):
                super(InsertSensorData, self).__init__()
                self.data = data or None

        @staticmethod
        def invoke(**kwargs=None): # TODO: Use kwargs to configure the command 
                                   #       execution
