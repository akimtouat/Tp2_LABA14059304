from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path="", static_folder="static")
app.config.from_object('config')
db = SQLAlchemy(app)
app.secret_key = "pioupiou"
, static_url_path="", static_folder="static"
