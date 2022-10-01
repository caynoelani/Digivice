#*********************************************
#******************IMPORTS********************
#*********************************************

#===================================
# Import connectToMySQL function
# Import App
#===================================
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

#=====================================
# Import Regex Module
#=====================================
import re
# create regular expressions
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,255}$')

#*********************************************
#*******************CLASS*********************
#*********************************************
class User:

   #===============================
   #Class attributes
   #===============================
   db = "digivice_schema"

   #===============================
   # Instance Constructor (init)
   #===============================

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

   #=============================
   # CREATE [one] instance
   #=============================
   @classmethod
   def create(cls, data):
      print("creating user")

      query = "INSERT INTO users ( username, email , password, created_at, updated_at) VALUES ( %(username)s , %(email)s , %(password)s , NOW(), NOW());"

      results = connectToMySQL(cls.db).query_db( query, data )

      return results

   #=============================
   # READ (one) by Email
   #=============================
   @classmethod
   def get_by_email(cls, data):

      print(f"retrieving one user from {cls.db}")

      query = "SELECT * FROM users WHERE email = %(email)s;"

      results = connectToMySQL(cls.db).query_db(query,data)

      print(f"here is the retrieved user: {results}")

      if len(results) < 1:
         return False
         
      return cls(results[0])

   # SELECT * FROM users JOIN favorites ON users.id = favorites.user_id WHERE users.id = %(id)s