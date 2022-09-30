from flask_app import app
from flask import redirect, render_template, session, request
from flask_app.models import user_model

@app.route('/login')
def render_login():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def user_login():
    print(request.form)
    return redirect('/')

@app.route('/register', methods=["POST"])
def user_register():
    print(request.form)
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')