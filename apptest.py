# apptest.py

from flask import Flask
from flask_restful import Resource, Api
#from flask_jwt_extended import jwt, jwt_required
from flask_jwt_extended import jwt_required

from security import authenticate, identity

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, Sandali):
        return {'student': 'Sandali'}

api.add_resource(Student, '/student/<string:Sandali>')
#http://127.0.0.1:5000/student/Rolf

app.run(port=5000)