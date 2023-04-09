from flask import Blueprint, request, render_template
import requests
import os

bp = Blueprint("handler", __name__, url_prefix="/handler")

access_token = None


def get_access_token(request_token):
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    url = f'https://github.com/login/oauth/access_token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={request_token}'
    headers = {
        'accept': 'application/json'
    }

    res = requests.post(url, headers=headers)

    if ("access_token" in list(res.json().keys())):
        return res.json()["access_token"]
    else:
        return -1


@bp.route("/access")
def access():
    global access_token
    request_token = request.args.get('code')
    token = get_access_token(request_token)

    if token == -1:
        return render_template("callback.html",
                               {"title": "Access denied", "desc": "Unable to fetch access token."})
    else:
        access_token = token
    return render_template("callback.html",
                           {"title": "Success", "desc": "User authenticated successfully."})


@bp.route("/user")
def user():
    if access_token is not None:
        url = 'https://api.github.com/user'
        headers = {"Authorization": 'token ' + access_token}

        res = requests.get(url=url, headers=headers)
        return res.json()
    else:
        return "Unauthorized"
