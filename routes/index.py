from flask import Blueprint, redirect
import os

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
def index():
    CLIENT_ID = os.environ.get("CLIENT_ID")
    return redirect(f'https://github.com/login/oauth/authorize?client_id={CLIENT_ID}')
