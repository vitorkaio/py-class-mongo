from .database import Database

class Perfil(Database):
  def __init__(self):
    Database.__init__(self) # Herda as props da class Database
    self._perfis = self._db['perfils']

  def getPerfil(self, id):
    return self._perfis.find_one({'_id': id})
