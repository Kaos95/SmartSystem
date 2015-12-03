#
# Crude version of sensor interface 
#
from flask import Flask
app = Flask(__name__)

import pymongo as PYMONGO
from flask import request

_DB = PYMONGO.MongoClient()
_DATA = "data"

@app.route('/sensor/', methods=["GET"])
def sensor():
	


@app.route("/sensor/<sensor_unit>/<sensor_id>/", methods=["GET","POST"])
def data(sensor_unit, sensor_id):
	sensordb = _DB[sensor_unit]
	
	if request.method == 'POST':
		# . Extract data from request
		return "in POST"
	elif request.method == 'GET':
		#TODO
		raise NotImplementedError()	

	return "Hello world"

if __name__ == '__main__':
	app.run()
