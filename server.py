from flask_app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', view = 'index')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html', view = 'favorites')

@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html', view = 'catalogue')

@app.route('/digimon')
def digimon():
    return render_template('digimon.html', view = 'digimon')

if __name__ == '__main__':
    app.run(debug=True)