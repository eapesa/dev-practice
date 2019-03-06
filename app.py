from flask import Flask
from flask import request
import json
import requests as http

app = Flask(__name__)

@app.route("/")
def index():
  return "This is my homepage"

user_list = [{'id':'1', 'name':'Elixa'}]
# GET http://localhost:5000/v1/users/<id>?param=name
# To test: curl -X GET -v -H "fb_token: FB_TOKEN" "http://localhost:5000/v1/users/<some-id>[?param=name]"
@app.route("/v1/users/<id>", methods=["GET"])
def users(id):
  for x in user_list:
    if x.get('id') == id:
      param = request.args.get('param')
      if not param:
        return "User details: {}".format(json.dumps(x))
      else:
        data = x.get(param)
        if not data:
          return "User details `{}` not found".format(param)
        else:
          return "User details `{}`: {}".format(param, data)

  token = request.headers.get('fb_token')
  fburl = 'https://graph.facebook.com/v3.2/me'
  qs = {'access_token':token, 'fields':'id,name,email,about,gender'}
  # Equivalent to curl -k -i -v -X GET https://graph.facebook.com/v3.2/me?fields=id,name,email,about,gender&access_token=FB_TOKEN
  headers = {'Content-Type': 'application/json'}
  r = http.get(fburl, params=qs, headers=headers, verify=False)
  fbdata = r.json()
  if fbdata.get('id'):
    param = request.args.get('param')
    if not param:
      return "User details: {}".format(json.dumps(fbdata))
    else:
      data = fbdata.get(param)
      if not data:
        return "User details `{}` not found".format(param)
      else:
        return "User details `{}`: {}".format(param, data)

  return "User not found"


  