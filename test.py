from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required
from security import authenticate, identity

# this is an example i got from stackoverflow. Author said that  the code is running but when i run it in conda 
# it again shows the same error message i stated on app.py

app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)  # Can easily add resources to this "app"

jwt = JWT(app, authenticate, identity)

items = []

# every resource has to be a class
class Item(Resource):
    @jwt_required()
    def get(self, name):

        item = next(filter(lambda x: x["name"] == name, items), None)

        return {"item": item}, 200 if item else 404

    def post(self, name):

        if next(filter(lambda x: x["name"] == name, items), None) is not None:
            return {"Message": "An Item with the name {} already exit".format(name)}, 400

        data = request.get_json()

        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201 # 201 is status code for created


class ItemList(Resource):

    def get(self):
        return {"items": items}



api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)


from werkzeug.security import safe_str_cmp
from .user import User

users = [
    User(1, "bob", "asdf")
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):

        return user


def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)

