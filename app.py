# app.py
#updated

from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required 
from security import authenticate

app = Flask(__name__)
app.secret_key = 'john'
api = Api(app)

class Student(Resource):
    def get(self, john):
        return {'student': 'john'}

api.add_resource(Student, '/student/<string:john>')
#http://127.0.0.1:5000/student/Rolf

app.run(port=5000)