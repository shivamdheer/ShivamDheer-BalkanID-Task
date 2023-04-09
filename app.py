from routes import index
from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)
app.register_blueprint(index.bp)
