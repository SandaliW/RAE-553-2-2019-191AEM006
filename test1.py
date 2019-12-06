# app.py
#updated

from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required 
#from security import authenticate

app = Flask(__name__)
app.secret_key = 'john'
api = Api(app)

class Student(Resource):
    def get(self, john):
        return {'student': 'john'}

api.add_resource(Student, '/student/<string:john>')
#http://127.0.0.1:5000/student/Rolf

app.run(port=5000)

# security.py

from werkzeug.security import safe_str_cmp
from user import User

user = [
   User(1, 'john', 'abcd')
]

username_mapping = {u.username: u for u in user}
userid_mapping = {u.id: u for u in user}

def authenticate(username, password):
   user = username_mapping.get(username, None)
   if user and safe_str_cmp(user.password ,password):

         return user

# user.py

class User:
     def __init__(self,_id, username, password):
         self.id = _id
         self.username = username
         self.password = password