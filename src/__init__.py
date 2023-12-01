# src/__init__.py
import os  # new
import sys


from flask import Flask, jsonify
from flask_restx import Resource, Api

# instantiate the app
app = Flask(__name__)
api = Api(app)
# set config
print(app.config, file=sys.stderr)
app_settings = os.getenv("APP_SETTINGS")  # new
app.config.from_object(app_settings)  # new


class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


api.add_resource(Ping, "/ping")
