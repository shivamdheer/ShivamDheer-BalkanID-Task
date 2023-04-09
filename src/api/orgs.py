from flask import Blueprint, request, redirect, render_template
from .init_db import connect, disconnect
import requests

bp = Blueprint("orgs", __name__, url_prefix="/user")

endpoint = "https://api.github.com"

conn, cur = connect()


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
        if len(res) > 0:
            orgs += res

        while len(res) > 0:
            page += 1
            res = get_org_by_page(access_token, page)[0]
            if len(res) > 0:
                orgs += res

        if (status == 200):
            for org in orgs:
                cur.execute("""
                    INSERT INTO owners (id, username, name, email, type)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE
                    SET username = EXCLUDED.username,
                    name = EXCLUDED.name,
                    email = EXCLUDED.email,
                    type = EXCLUDED.type;
                """, (org["id"], org["login"], org["name"], org["email"], org["type"]))
            conn.commit()
            disconnect(conn, cur)
            return {"count": len(orgs), "data": orgs}, status
        else:
            return render_template("error.html", title=status, desc=reason)
    else:
        return redirect("/")
