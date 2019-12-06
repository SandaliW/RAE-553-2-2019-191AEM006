# app.py
#updated

from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required 
from security import authenticate
# i always get an error when i execute with these lines. however i try i can't seem to find the correct answer. 
#from flask_jwt_extended import JWT, jwt_required and from security import authenticate, idenetity
# but without JWT and identity code will run but then again i am geeting 404 at postman

app = Flask(__name__)
app.secret_key = 'john'
api = Api(app)

class Student(Resource):
    def get(self, john):
        return {'student': 'john'}

api.add_resource(Student, '/student/<string:john>')
#http://127.0.0.1:5000/student/Rolf

app.run(port=5000)
