from flask import Blueprint, Response
from .init_db import connect, disconnect
import io
import csv

bp = Blueprint("download", __name__, url_prefix="/download")

endpoint = "https://api.github.com"


@ bp.route("/")
def download():
    conn, cur = connect()
    cur.execute("""
    SELECT owners.id, owners.username, owners.name, owners.email,
    repos.id, repos.name, repos.status, repos.stars
    FROM owners JOIN repos ON owners.id = repos.oid;
    """)
    conn.commit()
    data = cur.fetchall()
    disconnect(conn, cur)

    output = io.StringIO()
    writer = csv.writer(output)

    cols = [
        "Owner ID", "Owner Username", "Owner Name", "Owner Email", "Repo ID", "Repo Name", "Status", "Stars"]
    writer.writerow(cols)

    for row in data:
        writer.writerow([str(i) if i is not None else "" for i in row])

    output.seek(0)

    return Response(output, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=download.csv"})
