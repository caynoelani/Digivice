from flask_app import app
from flask import redirect, render_template, session
from flask_app.models import user_model, digimon_model

@app.route('/')
def render_index():
    return render_template('index.html', view = 'index')

@app.route('/home')
def render_home():
    return redirect('/')

@app.route('/favorites')
def render_favorites():
    return render_template('favorites.html', view = 'favorites')

@app.route('/catalogue')
def render_catalogue():
    return render_template('catalogue.html', view = 'catalogue')

@app.route('/digimon')
def render_digimon():
    return render_template('digimon.html')