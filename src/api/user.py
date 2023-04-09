from flask import Blueprint, request, redirect, render_template
from .init_db import connect, disconnect
import requests

bp = Blueprint("user", __name__, url_prefix="/user")

endpoint = "https://api.github.com"

conn, cur = connect()


@ bp.route("/")
def user():
    access_token = request.cookies.get('access_token')
    if access_token is not None:
        url = f'{endpoint}/user'
        headers = {"Authorization": 'token ' + access_token}

        res = requests.get(url=url, headers=headers)
        data = res.json()

        if (res.status_code == 200):
            cur.execute("""
                INSERT INTO owners (id, username, name, email, type)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE
                SET username = EXCLUDED.username,
                name = EXCLUDED.name,
                email = EXCLUDED.email,
                type = EXCLUDED.type;
                """, (data["id"], data["login"], data["name"], data["email"], data["type"]))
            conn.commit()
            disconnect(conn, cur)
            return {"id": data["id"], "username": data["login"],
                    "name": data["name"], "email": data["email"], "type": data["type"]}, res.status_code
        else:
            render_template("error.html", title=res.status_code,
                            desc=res.reason)
    else:
        return redirect("/")
