#! /usr/bin/python

#
# Client interface to storage rest api
#
import requests


def main():
	data = {"first":"value", "second":"value", "third":"value"}
	res = requests.post( "http://localhost:5000/sensor/RaspberryPi/temperature", data=data)
	print res.text

if __name__ == '__main__':
	main()
