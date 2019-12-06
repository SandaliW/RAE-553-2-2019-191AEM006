# security.py

from werkzeug.security import safe_str_cmp
from user import User

user = [
   User(1, 'rolf', 'abcd')
]

username_mapping ={u.username: u for u in users}

userid_mapping ={u.id: u for u in users}

def authenticate(username, password):
 user=username_mapping.get(username, None)

if user and safe_str_cmp(user.password ,password):
return user
