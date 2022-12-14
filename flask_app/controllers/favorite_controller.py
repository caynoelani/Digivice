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
from flask import render_template, redirect, request, flash, session, url_for
import requests, json, functools


#=====================================
# Import Controllers
#=====================================
from flask_app.controllers.user_controller import login_required

#=====================================
# Import Models
#=====================================
from flask_app.models import favorite_model, user_model, digimon_model

#******************************************************
#**********************Decorators**********************
#******************************************************

#=====================================
# Login Required Decorator
#=====================================
def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        else:
            flash("Please login")
            return redirect(url_for('login_page'))
    return wrapper


#******************************************************
#***********************ROUTES*************************
#******************************************************

#=====================================
# Favorites Page Route
#=====================================
@app.route('/favorites')
async def favorites_page():
    is_logged_in = user_model.User.validate_logged_in()

    if is_logged_in:

        data = {
            "user_id" : session["user_id"]
        }

        user_with_favorites = user_model.User.get_user_with_favorites(data)

        if len(user_with_favorites.favorites) > 0:
            favorite_reqs = []

            for favorite in user_with_favorites.favorites:
                favorite_reqs.append(favorite.number)

            favorite_list = await digimon_model.get_digimon_info(favorite_reqs)

        else:
            favorite_list = False

        return render_template('favorites.html', favorite_list = favorite_list)
    
    return redirect(url_for('login_page'))

#=====================================
# Create Favorite Route [POST]
#=====================================
@app.route('/favorites/add/<req>')
def create_favorite(req):

    if user_model.User.validate_logged_in():
        data = {
            "user_id" : session["user_id"],
            "digimon_id" : req
        }

        favorite_id = favorite_model.Favorite.create_favorite(data)

        return redirect(f'/digimon/{data["digimon_id"]}')

    else:
        flash("Please Log In")
        return redirect('/login')

#=====================================
# Delete Favorite Route [POST]
#=====================================
@app.route('/favorites/delete/<req>')
def delete_favorite(req):

    data = {
        "user_id" : session["user_id"],
        "digimon_number" : req
    }

    favorite_model.Favorite.delete_favorite_by_number(data)

    return redirect('/favorites')