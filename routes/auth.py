from flask import Blueprint, request
import os

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/callback")
def callback():
    request_token = request.args.get('code')
    return request_token
