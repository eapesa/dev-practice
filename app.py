from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "This is my homepage"

user_list = [{"id":"1","name":"Raleine"}]
# GET http://localhost:5000/v1/users/id?param=name
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
  return "User not found"

