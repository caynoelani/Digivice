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
# Search Route
#=====================================