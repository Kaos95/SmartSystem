#
# Application globals
#
# @author: Hayden McParlane
# @creation-date: 12.23.2015

# JSON data format
UNIT_ID = 'unit_id'
SENSOR_ID = 'sensor_id'
PAYLOAD = 'payload'

STANDARD_DATA_KEYS = [UNIT_ID, SENSOR_ID, PAYLOAD]

# REST URLS STORAGE
REST_HOST_STORAGE = '159.203.246.108'
REST_PORT_STORAGE = 5000
REST_BASE_STORAGE = 'http://{}:{}'.format(REST_HOST_STORAGE, REST_PORT_STORAGE)

REST_SENSORS = 'sensors'
REST_SENSOR = 'sensor'
REST_DATA = 'data'
