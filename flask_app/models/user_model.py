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

#===================================
# Validate Register
#===================================
   @staticmethod
   def validate_register(data):
      is_valid = True

      if len(data['username']) < 2:
         flash("Username must be at least 2 characters.")
         is_valid = False

      if not EMAIL_REGEX.match(data['email']): 
         flash("Invalid email address!")
         is_valid = False
      elif EMAIL_REGEX.match(data['email']): 
         query = "SELECT * FROM users;"
         results = connectToMySQL(User.db).query_db(query)

         for dictionary in results:
               if data['email'] == dictionary['email']:
                  flash("email already exists")
                  is_valid = False

      if data['password'] != data['confirmPassword']:
         flash("Passwords do not match.")
         is_valid = False
      if not PASSWORD_REGEX.match(data['password']): 
         flash("Password must have at least one uppercase letter, one lowercase letter, one number, and be 8-255 characters in length!")
         is_valid = False

      return is_valid

#===================================
# Validate Login
#===================================
   @staticmethod
   def validate_login(data):
      is_valid = True

      user_in_db = User.get_by_email(data)

      if not user_in_db:
         flash("Invalid email or password")
         is_valid = False
      
      elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
         flash("Invalid email or password")
         is_valid = False
         
      return is_valid


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