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
