from replit import db

db['users'] = []
users = db['users']

print(users)

new_user = {"name": "bobby"}
db['users'].append(new_user)
users = db['users']
print(users)
db.