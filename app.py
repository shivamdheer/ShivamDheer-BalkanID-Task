from routes import auth, index
from flask import Flask, request, redirect, url_for

app = Flask(__name__)
app.register_blueprint(index.bp)
app.register_blueprint(auth.bp)
