from flask import Blueprint
import os

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
def index():
    return os.environ.get("CLIENT_ID")
