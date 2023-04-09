from flask import Blueprint, request, redirect, render_template
import requests

bp = Blueprint("handler", __name__, url_prefix="/user")

access_token = None
endpoint = "https://api.github.com"


@ bp.route("/")
def user():
    if access_token is not None:
        url = f'{endpoint}/user'
        headers = {"Authorization": 'token ' + access_token}

        res = requests.get(url=url, headers=headers).json()
        # data = {"id": res["login"], "name": res["name"]}
        # if res["email"] is not None:
        #     data["email"] = res["email"]
        return res
    else:
        return render_template("callback.html", title="Access denied", desc="You are unauthorized.")
