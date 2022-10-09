#******************************************************
#***********************IMPORTS************************
#******************************************************

#=====================================
# Import app
#=====================================
from pydoc import classname
from flask_app import app

#=====================================
# Import Modules/Packages
#=====================================
from flask import render_template, redirect, request, flash, session, jsonify
import requests, json, os, random

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
async def search_one_digimon():

    req = request.form["indexSearchbar"]

    if req.isnumeric():
        return redirect(f'/digimon/{int(req)}')

    elif req.isalpha():
        try:
            req = req.lower()
            return redirect(f'/digimon/{req}')

        except requests.exceptions.JSONDecodeError:
            flash('Please check your spelling and try again')
            return redirect('/')

    else:
        flash("Please enter a valid name or number")
        return redirect('/')

#=====================================
# Digimon Catalogue Page Route
#=====================================s
# @app.route('/digimon')
# async def read_all_digimon():
#     is_logged_in = user_model.User.validate_logged_in()

#     digimon_list = await digimon_model.get_digimon_list()
    
#     return render_template('digimon.html', is_logged_in = is_logged_in, digimon_list = digimon_list)

#=====================================
# Digimon [ONE] Page Route
#=====================================
@app.route('/digimon/<req>')
async def read_one_digimon(req):

    if req.isalpha() or req.isnumeric():

        digimon_info = await digimon_model.get_digimon_info(req)

    if 'error' in digimon_info:
        flash("Please enter a valid name or number")
        return redirect('/')

    is_logged_in = user_model.User.validate_logged_in()

    if is_logged_in:

        data = {
            "digimon_number" : req,
            "user_id" : session["user_id"]
        }

        is_favorited = user_model.User.validate_favorited(data)

        print(is_favorited)

    return render_template('digimon.html', digimon_info = digimon_info, is_favorited = is_favorited)