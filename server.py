from flask_app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', view = 'index')

@app.route('/about')
def about():
    return render_template('about.html', view = 'about')

@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html', view = 'catalogue')

# @app.route('/catalogue/<id>')
# def catalogue(id):
#     return render_template('index.html', view = 'catalogue/<id>')

if __name__ == '__main__':
    app.run(debug=True)