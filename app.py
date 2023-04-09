from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)


@app.route("/")
def index():
    return os.environ.get("CLIENT_ID")
