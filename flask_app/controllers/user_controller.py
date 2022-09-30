from flask_app import app
from flask import redirect, render_template, session, request
from flask_app.models import user_model

@app.route ('/login')
def user_login():
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')