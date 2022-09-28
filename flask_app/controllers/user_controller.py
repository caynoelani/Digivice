from flask_app import app
from flask import redirect, render_template, session, request
from flask_app.models import user_model


@app.route('/logout', methods='POST')
def logout():
    session.clear()
    return redirect('/')