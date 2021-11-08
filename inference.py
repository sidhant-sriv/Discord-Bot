import requests
import json

# Make a post request with json data to localhost:5000/postjson
data = {
    "image_url": "https://i.imgur.com/lrSkIM1.jpeg"
}
url = "http://localhost:5000/postjson"
r = requests.post(url, json=data).json()
print(r['data'])
