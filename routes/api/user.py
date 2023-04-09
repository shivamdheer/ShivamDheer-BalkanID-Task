from flask import Blueprint, request, redirect, render_template
import requests

bp = Blueprint("user", __name__, url_prefix="/user")

endpoint = "https://api.github.com"


@ bp.route("/")
def user():
    access_token = request.cookies.get('access_token')
    if access_token is not None:
        url = f'{endpoint}/user'
        headers = {"Authorization": 'token ' + access_token}

        res = requests.get(url=url, headers=headers)
        data = res.json()

        if (res.status_code == 200):
            return {"id": data["id"], "username": data["login"],
                    "name": data["name"], "email": data["email"], "type": data["type"]}, res.status_code
        else:
            render_template("error.html", title=res.status_code,
                            desc=res.reason)
    else:
        return redirect("/")
