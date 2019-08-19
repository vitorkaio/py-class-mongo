from .database import Database

# Herda da classe Database
class User(Database):
  def __init__(self):
    Database.__init__(self) # Herda as props da class Database
    self._users = self._db['users']
  
  def getUsers(self):
    users = []
    for user in self._users.find({}):
      users.append(user)
    return users

  def insertUser(self, user):
    try:
      self._users.insert_one(user)
      return True
    except Exception as err:
      return err.args[0]

