#===================================================
#Imports
#===================================================
import pymysql.cursors
import os

#===================================================
# Class w/ instance of connection to database
#===================================================
class MySQLConnection:
    def __init__(self, db):
        #===========================================
        # User/PW must match local instance in mysql
        #===========================================
        connection = pymysql.connect(host = 'localhost',
                                    user = os.getenv("PYMYSQL_USER"), 
                                    password = os.getenv("PYMYSQL_PASSWORD"), 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        #===========================================
        # Connection to the database
        #===========================================
        self.connection = connection

    #===============================================
    # Method to query the database
    #===============================================
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    #==================================
                    # INSERT queries return ID 
                    # of the row inserted
                    #==================================
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    #==================================
                    # SELECT queries returns db data 
                    # always as a LIST OF DICTIONARIES
                    #==================================
                    result = cursor.fetchall()
                    return result
                else:
                    #==================================
                    # UPDATE and DELETE queries
                    # will return nothing
                    #==================================
                    self.connection.commit()
            # except Exception as e:
            #     # if query fails, method returns FALSE
            #     print("Something went wrong", e)
            #     return False
            finally:
                #=======================================
                # close the connection
                #=======================================
                self.connection.close() 

#=======================================================
# ConnectToMySQL receives our database
# Uses db to create instance of MySQLConnection
#=======================================================
def connectToMySQL(db):
    return MySQLConnection(db)

