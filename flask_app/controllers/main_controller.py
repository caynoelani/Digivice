#******************************************************
#***********************IMPORTS************************
#******************************************************

#=====================================
# Import app
#=====================================
from flask_app import app

#=====================================
# Import Modules/Packages
#=====================================
from flask import redirect, render_template, session

#=====================================
# Import Models
#=====================================
from flask_app.models import favorite_model, user_model, digimon_model


#******************************************************
#***********************ROUTES*************************
#******************************************************

#=====================================
# Index Routes
#=====================================
@app.route('/')
@app.route('/home')
def index_page():

    is_logged_in = user_model.User.validate_logged_in()

    return render_template('index.html', view = 'index', is_logged_in = is_logged_in)

#=====================================
# Catalogue Page Routes
#=====================================    
@app.route('/catalogue')
def catalogue_page():
    is_logged_in = user_model.User.validate_logged_in()

    return render_template('catalogue.html', view = 'catalogue', is_logged_in = is_logged_in)