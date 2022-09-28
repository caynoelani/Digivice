from flask_app import app
from flask_app.models import user_model, digimon_model
from flask import render_template, redirect, request, flash, session
import requests
import json


