from flask import Blueprint, request, render_template

bp = Blueprint("index", __name__, url_prefix="/")

endpoint = "https://api.github.com"


@bp.route("/")
def index():
    if request.cookies.get('access_token') is not None and request.cookies.get('user') is not None:
        return render_template("index.html", authorized=True, user=request.cookies.get('user'))
    else:
        return render_template("index.html")
