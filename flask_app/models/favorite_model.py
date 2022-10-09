#*********************************************
#******************IMPORTS********************
#*********************************************

#===================================
# Import connectToMySQL function
# Import App
#===================================
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers.favorite_controller import favorites_page

#*********************************************
#*******************CLASS*********************
#*********************************************
class Favorite:

    #===============================
    #Class attributes
    #===============================
    db = "digivice_schema"

    #===============================
    # Instance Constructor (init)
    #===============================
    def __init__(self, data):
        self.id = data["id"]

        self.number = data["number"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.user = {}

    def __repr__(self):
        return f"Digimon #{self.number}"


#*********************************************
#***************STATIC METHODS****************
#*********************************************



#*********************************************
#************CLASS METHODS (CRUD)*************
#*********************************************
    #=============================
    # Create Favorite
    #=============================
    @classmethod
    def create_favorite(cls, data):
        favorite = cls.get_favorite_by_number(data)

        if favorite:
            print("already favorited")
            return False
            
        query = "INSERT INTO favorites (number, created_at, updated_at, user_id) VALUES (%(digimon_id)s, NOW(), NOW(), %(user_id)s)"

        results = connectToMySQL(cls.db).query_db(query, data)

        return results

    #=============================
    # READ (one) by id
    #=============================
    @classmethod
    def get_favorite_by_number(cls, data):

        query = "SELECT * FROM favorites WHERE number = %(digimon_id)s;"

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        if len(results) < 1:
            return False
            
        return cls(results[0])