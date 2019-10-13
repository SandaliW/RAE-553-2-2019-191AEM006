# app.py

from flask import Flask
#from flask import jsonif,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#########@app.route('/', methods=['GET'])
class Student(Resource):
    def get(self, Sandali):
        return ('student',Sandali)

api.add_resource(Student, '/student/<string:Sandali>')

app.run(port=5000)