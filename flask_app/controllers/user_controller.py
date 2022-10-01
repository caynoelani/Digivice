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
from flask import redirect, render_template, session, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#=====================================
# Import Models
#=====================================
from flask_app.models import user_model

#******************************************************
#***********************ROUTES*************************
#******************************************************

#=====================================
# Login Routes
#=====================================
@app.route('/login')
def render_login():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def user_login():
    
    if request.form["form_type"] == "login":
        session["email"] = request.form["email"]
    elif request.form["form_type"] == "register":
        session["username"] = request.form["username"]
        session["email"] = request.form["email"]
    return redirect('/')

#=====================================
# Logout Route
#=====================================
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    print("user logged out")
    return redirect('/')