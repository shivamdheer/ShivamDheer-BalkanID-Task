from flask import Blueprint, request, redirect, render_template, make_response
import os
import requests

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/")
def auth():
    CLIENT_ID = os.environ.get("CLIENT_ID")
    scopes = ["read:user", "user:email", "read:org", "repo"]
    return redirect(f'https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope={"%20".join(scopes)}')


def get_access_token(request_token):
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    url = f'https://github.com/login/oauth/access_token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={request_token}'
    headers = {
        'accept': 'application/json'
    }

    res = requests.post(url, headers=headers)

    if ("access_token" in list(res.json().keys())):
        return res.json()["access_token"], res.status_code, res.reason
    else:
        return -1, res.status_code, res.reason


@bp.route("/callback")
def callback():
    if request.args.get('error') is not None:
        return render_template("error.html", title=request.args.get('error'), desc=request.args.get('error_description'))

    request_token = request.args.get('code')
    access_token, status, reason = get_access_token(request_token)

    if access_token == -1:
        return render_template("error.html", title=status, desc=reason)
    else:
        res = make_response(redirect("/user"))
        res.set_cookie('access_token', access_token)
    return res
# render_template("error.html", title="Success", desc="User authenticated successfully.")
