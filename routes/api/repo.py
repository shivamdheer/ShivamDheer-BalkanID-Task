from flask import Blueprint, request, redirect, render_template
import requests

bp = Blueprint("handler", __name__, url_prefix="/repo")

access_token = None
endpoint = "https://api.github.com"


@ bp.route("/")
def repo():
    if access_token is not None:
        url = f'{endpoint}/user/repos'
        headers = {"Authorization": 'token ' + access_token}
        params = {"page": 1, "per_page": 100}

        res = requests.get(url=url, headers=headers, params=params).json()
        return res
    else:
        return render_template("callback.html", title="Access denied", desc="You are unauthorized.")
