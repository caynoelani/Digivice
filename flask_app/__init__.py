from flask import Flask, session
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")