#
# RESTful Controller API
#
# @author: Hayden McParlane
# @creation-date: 1.1.2016
import flask
from flask import Flask

app = Flask(__name__)

@app.route('/event/', methods=["POST"])
def invoke_event(event_id):
	# Read in JSON post
	event = 

	# Parse event JSON

	# Invoke appropriate response

if __name__=='__main__':
	app.run()
