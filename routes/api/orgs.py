from flask import Blueprint, request, redirect, render_template
import requests

bp = Blueprint("orgs", __name__, url_prefix="/user")

endpoint = "https://api.github.com"


def get_org_by_page(access_token, page):
    url = f'{endpoint}/user/orgs'
    headers = {"Authorization": 'token ' + access_token}
    params = {"page": page, "per_page": 100}

    res = requests.get(url=url, headers=headers, params=params)

    orgs = []
    for org in res.json():
        orgs.append({"id": org["id"], "username": org["login"],
                     "name": org["name"], "email": org["email"], "type": org["type"]})
    return orgs, res.status_code, res.reason


@ bp.route("/orgs")
def orgs():
    access_token = request.cookies.get('access_token')
    if access_token is not None:
        orgs = []
        page = 1

        res, status, reason = get_org_by_page(access_token, page)
        orgs.append(res)

        while len(res) > 0:
            page += 1
            res = get_org_by_page(access_token, page)
            if len(res) > 0:
                orgs.append(res)

        if (status == 200):
            return orgs, status
        else:
            return render_template("callback.html", title=status, desc=reason)
    else:
        return redirect("/")
