# from controller.database import Database
from controller.user import User
from controller.perfil import Perfil
from datetime import datetime as Date
from bson.objectid import ObjectId

user = User()
perfil = Perfil()

newUser = {
  'name': 'Alice',
  'password': '369258147',
  'email': 'alice@email.com',
  'create_data': Date.now(),
  'perfis': [
    ObjectId("5d52ffed4cd29474379dab54")
  ]
}

res = user.insertUser(newUser)
print(res)

users = user.getUsers()

for userItem in users:
  print(userItem['name'])
  for perfilItem in userItem['perfis']:
    res = perfil.getPerfil(perfilItem)
    print(res['name'])
  print('\n')

