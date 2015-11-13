#
# The sensor interface 
#

from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

import pymongo as PYMONGO
from flask import request

_MONGO_CLIENT = PYMONGO.MongoClient()
_API = flask_restful.Api

_DATA = 'data'

class SensorContext(Resource):
	def get(self):
		

@app.route('/sensor/<sensor_unit>/<sensor_id>/', methods=['GET', 'POST'])
def data(sensor_unit, sensor_id):
	sensordb = _MONGO_CLIENT[sensor_unit]
	json = None
	if request.method == 'POST':
		# . Extract data from request
		data = request.form[_DATA]
		json = {"reached":"POST", "sensor_unit":sensor_unit, "sensor_id":sensor_id}
		return json
	elif request.method == 'GET':
		#TODO
		raise NotImplementedError()

#
# Resource definitions
#
api.add_resource(SensorContext, '/sensor/')

if __name__ == '__main__':
	app.run()
