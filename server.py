from flask_app import app
from flask import render_template

@app.route('/')
def server_test():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)