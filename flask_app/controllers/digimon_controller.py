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
from flask import render_template, redirect, request, flash, session, jsonify
import requests, json, os

#=====================================
# Import Models
#=====================================
from flask_app.models import favorite_model, user_model, digimon_model


#******************************************************
#***********************ROUTES*************************
#******************************************************

#=====================================
# Search Route [POST]
#=====================================
@app.route('/digimon/search', methods=['POST'])
async def search_digimon():

    req = request.form["indexSearchbar"]

    if req.isalpha() or req.isnumeric():
        try:
            req = req.lower()

        except requests.exceptions.JSONDecodeError:
            flash('Please check your spelling and try again')
            return redirect('/')

    else:
        flash("Please enter a digimon's name or number")
        return redirect('/')

        
    print(f"----------------- {digimon_info['name']} -----------")
    return redirect('/digimon/<digimon_info>')

#=====================================
# Digimon Page Routes
#=====================================
@app.route('/digimon')
def render_digimon():
    is_logged_in = user_model.User.validate_logged_in()
    
    return render_template('digimon.html', is_logged_in = is_logged_in)

#=====================================
# 
#=====================================
@app.route('/digimon/<req>',)
def read_one_digimon(req):

    # is_logged_in = user_model.User.validate_logged_in()

    # if session['user_id']:
    #     data = { "user_id": session["user_id"]}
    #     user = user_model.User.get_user_by_id(data)

    digimon_info = await digimon_model.get_digimon_info(req)

    return render_template('digimon.html')