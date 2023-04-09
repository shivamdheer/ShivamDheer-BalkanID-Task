from flask import Blueprint, request, redirect
import os

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/")
def index():
    CLIENT_ID = os.environ.get("CLIENT_ID")
    return redirect(f'https://github.com/login/oauth/authorize?client_id={CLIENT_ID}')


@bp.route("/callback")
def callback():
    request_token = request.args.get('code')
    return redirect(f'/handler/access?code={request_token}')
