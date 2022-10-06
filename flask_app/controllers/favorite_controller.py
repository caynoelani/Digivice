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
from flask import render_template, redirect, request, flash, session
import requests
import json

#=====================================
# Import Models
#=====================================
from flask_app.models import favorite_model, user_model, digimon_model


#******************************************************
#***********************ROUTES*************************
#******************************************************
#=====================================
# Favorite Route [POST]
#=====================================
@app.route('/digimon/favorites/add', methods=['POST'])
def add_favorite():

    if user_model.User.validate_logged_in():
        data = {
            "user_id" : session["user_id"],
            "digimon_id" : request.form["digimon_id"]
        }

        favorite_id = favorite_model.Favorite.create_favorite(data)

        return redirect(f'/digimon/{int(data["digimon_id"])}', favorite_id = favorite_id)

    else:
        flash("Please Log In")
        return redirect('/login')