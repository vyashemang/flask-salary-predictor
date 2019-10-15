import requests

# URL
url = 'http://localhost:5000/api/'

# Change the value of experience that you want to test
payload = {
	'exp':1.8
}

r = requests.post(url,json=payload)

print(r.json())
