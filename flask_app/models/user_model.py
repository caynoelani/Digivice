#*********************************************
#******************IMPORTS********************
#*********************************************

#===================================
# Import connectToMySQL function
# Import App
#===================================
from mysqlconnection import connectToMySQL
from flask_app import app

#*********************************************
#*******************CLASS*********************
#*********************************************

class User:
   def __init__(self, data):
      self.id = data["id"]

      self.username = data["username"]
      self.email = data["email"]
      
      self.password = data["password"]
      self.created_at = data["created_at"]
      self.updated_at = data["updated_at"]


#*********************************************
#***************STATIC METHODS****************
#*********************************************



#*********************************************
#************CLASS METHODS (CRUD)*************
#*********************************************

   # SELECT * FROM users JOIN favorites ON users.id = favorites.user_id WHERE users.id = %(id)s