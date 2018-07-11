import requests

def get_data():
	# 'https://sanction.seva.capitalfloat.com/v1/sanction/73764305-0be7-4e28-8f56-d20176148824'
	url = 'https://sanction.seva.capitalfloat.com/v1/sanction/73764305-0be7-4e28-8f56-d20176148824'

	r = requests.get(url)
	data = r.json()

	# data = { "_id" : "01001", "city" : "AGAWAM", "loc" : [ -72.622739, 42.070206 ], "pop" : 15338, "state" : "MA" }

	return data

