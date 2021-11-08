from flask import Flask
from flask import request
import requests
api_key = 'key'
api_secret = 'key do you love me'
def make_classification(image_url):
    response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))
    res = []
    obj = response.json()
    for i in range(3):
        t = dict()
        t['confidence'] = obj['result']['tags'][i]['confidence']
        t['classification'] = obj['result']['tags'][i]['tag']['en']
        res.append(t)
    return {"data": res}


 
app = Flask(__name__)
  

@app.route('/predict', methods = ['POST'])
def postJsonHandler():
    content = request.get_json()
    return make_classification(content['image_url'])
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090)