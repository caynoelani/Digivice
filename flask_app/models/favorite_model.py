#*********************************************
#******************IMPORTS********************
#*********************************************

#===================================
# Import connectToMySQL function
# Import App
#===================================
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

#*********************************************
#*******************CLASS*********************
#*********************************************
class Favorite:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]
        self.nickname = data["nickname"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


#*********************************************
#***************STATIC METHODS****************
#*********************************************



#*********************************************
#************CLASS METHODS (CRUD)*************
#*********************************************