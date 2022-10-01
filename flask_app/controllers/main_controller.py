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
    return render_template('index.html', view = 'index')

@app.route('/home')
def render_home():
    return redirect('/')

#=====================================
# Favorites Page Routes
#=====================================
@app.route('/favorites')
def render_favorites():
    return render_template('favorites.html', view = 'favorites')

#=====================================
# Catalogue Page Routes
#=====================================    
@app.route('/catalogue')
def render_catalogue():
    return render_template('catalogue.html', view = 'catalogue')

#=====================================
# Digimon Page Routes
#=====================================
@app.route('/digimon')
def render_digimon():
    return render_template('digimon.html')