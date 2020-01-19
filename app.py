#app.py


from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required # set JWT work with the app we are creating

from security import authenticate, identity  #permit the authentication of the user

#we make a list of musical instruments
items_List = {
    "Item_1": {
        "Item": "Guitar",
        "Price": "$90"
    },
    "Item_2": {
        "Item": "Piano",
        "Price": "$300"
    }
}

app = Flask(__name__)
app.secret_key = 'music'
api = Api(app)

class Items(Resource):
    def get (self):
        return items_List  #here we return the item list

class Item(Resource):
    def get(self, name):
        return items_List[name]
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("Item")
        args = parser.parse_args()
        items_List[name] = {"Item": args["Item"]}
        return items_List[name]
    def post(self, name):
        if name in items_List:
            parser = reqparse.RequestParser()
            parser.add_argument("Item")
            args = parser.parse_args()
            items_List[name]["Item"] = args["Item"]
            return items_List[name]
        return {"message": "Item {} not in the items_List".format(name)}
    def delete(self, name):
        if name in items_List:
            items_List.pop(name)
            return items_List
        return {"message": "Item {} not in the items_List".format(name)}


api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')

#http://127.0.0.1:5000/item/Item_1
#http://127.0.0.1:5000/item/Item_2

#when we choose the methos we want GET, PUT, POST, DELETE 
#for above two urls, resilts will also be given respectively

app.run(port=5000)