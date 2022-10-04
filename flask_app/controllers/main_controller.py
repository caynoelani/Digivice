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
def render_index():

    is_logged_in = user_model.User.validate_logged_in()

    return render_template('index.html', view = 'index', is_logged_in = is_logged_in)

@app.route('/home')
def render_home():
    return redirect('/')

#=====================================
# Favorites Page Routes
#=====================================
@app.route('/favorites')
def render_favorites():
    is_logged_in = user_model.User.validate_logged_in()

    if is_logged_in:
        return render_template('favorites.html', view = 'favorites', is_logged_in = is_logged_in)
    
    return redirect('/login')

#=====================================
# Catalogue Page Routes
#=====================================    
@app.route('/catalogue')
def render_catalogue():
    is_logged_in = user_model.User.validate_logged_in()

    return render_template('catalogue.html', view = 'catalogue', is_logged_in = is_logged_in)