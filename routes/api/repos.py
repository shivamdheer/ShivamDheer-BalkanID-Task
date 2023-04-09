from flask import Blueprint, request, redirect, render_template
import requests

bp = Blueprint("repos", __name__, url_prefix="/user")

endpoint = "https://api.github.com"


def get_repo_by_page(access_token, page):
    url = f'{endpoint}/user/repos'
    headers = {"Authorization": 'token ' + access_token}
    params = {"page": page, "per_page": 100}

    res = requests.get(url=url, headers=headers, params=params)

    repos = []
    for repo in res.json():
        repos.append({"id": repo["id"], "name": repo["name"], "oid": repo["owner"]
                      ["id"], "status": "private" if repo["private"] else "public", "stars": repo["stargazers_count"]})
    return repos, res.status_code, res.reason


@ bp.route("/repos")
def repos():
    access_token = request.cookies.get('access_token')
    if access_token is not None:
        repos = []
        page = 1

        res, status, reason = get_repo_by_page(access_token, page)
        if len(res) > 0:
            repos.append(res)

        while len(res) > 0:
            page += 1
            res = get_repo_by_page(access_token, page)
            if len(res) > 0:
                repos.append(res)

        if (status == 200):
            return repos, status
        else:
            return render_template("error.html", title=status, desc=reason)
    else:
        return redirect("/")
