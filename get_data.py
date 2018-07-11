import requests

def get_data():
	url = 'ENTER URL'

	r = requests.get(url)
	data = r.json()

	# data = { "_id" : "01001", "city" : "AGAWAM", "loc" : [ -72.622739, 42.070206 ], "pop" : 15338, "state" : "MA" }

	return data

