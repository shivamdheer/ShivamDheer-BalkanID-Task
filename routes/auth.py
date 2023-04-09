from flask import Blueprint, request, redirect, render_template
import os

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/")
def index():
    CLIENT_ID = os.environ.get("CLIENT_ID")
    scopes = ["read:user", "user:email", "repo"]
    return redirect(f'https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope={"%20".join(scopes)}')


@bp.route("/callback")
def callback():
    if request.args.get('error') is not None:
        return render_template("callback.html",
                               {"title": request.args.get('error'), "desc": request.args.get('error_description')})
    request_token = request.args.get('code')
    return redirect(f'/access?code={request_token}')
