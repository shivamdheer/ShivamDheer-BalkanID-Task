from flask import Blueprint, request, redirect, render_template
import requests

bp = Blueprint("repos", __name__, url_prefix="/repos")

endpoint = "https://api.github.com"


def get_repo_by_page(access_token, page):
    url = f'{endpoint}/user/repos'
    headers = {"Authorization": 'token ' + access_token}
    params = {"page": page, "per_page": 100}

    res = requests.get(url=url, headers=headers, params=params).json()

    repos = []
    for repo in res:
        repos.append({"id": repo["id"], "name": repo["name"], "oid": repo["owner"]
                      ["id"], "status": "private" if repo["private"] else "public", "stars": repo["stargazers_count"]})
    return repos


@ bp.route("/")
def repo():
    access_token = request.cookies.get('access_token')
    if access_token is not None:
        repos = []
        page = 1

        res = get_repo_by_page(access_token, page)
        repos.append(res)

        while len(res) > 0:
            page += 1
            res = get_repo_by_page(access_token, page)
            repos.append(res)
        return repos
    else:
        return render_template("callback.html", title="Access denied", desc="You are unauthorized.")
