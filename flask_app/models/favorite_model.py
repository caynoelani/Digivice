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

    #===============================
    #Class attributes
    #===============================
    db = "digivice_schema"

    #===============================
    # Instance Constructor (init)
    #===============================
    def __init__(self, data):
        self.id = data["id"]

        self.user_id = data["user_id"] #foreign key

        self.number = data["digimon_id"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


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
        query = "INSERT INTO favorites (number, create_at, updated_at(), user_id) VALUES (%(digimon_id)s, NOW(), NOW(), %(user_id)s"

        results = connectToMySQL(cls.db).query_db(query, data)
        pass

        return results

    #=============================
    # READ (GET ALL) Favorites
    #=============================
    @classmethod
    def get_favorite_by_user(cls, data):

        query = "SELECT * FROM favorites WHERE user_id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)

        favorites_list = []

        if not results:
            return False
        
        for digimon in results:
            favorites_list.append(cls(digimon))
        
        return favorites_list

#    SELECT * FROM users JOIN favorites ON users.id = favorites.user_id WHERE users.id = %(id)s