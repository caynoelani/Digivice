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
from flask_app.models import favorite_model, user_model


#******************************************************
#***********************ROUTES*************************
#******************************************************