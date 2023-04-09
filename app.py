from src import auth, index
from src.api import repos, user, orgs, download
from flask import Flask

app = Flask(__name__)
app.register_blueprint(index.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(user.bp)
app.register_blueprint(repos.bp)
app.register_blueprint(orgs.bp)
app.register_blueprint(download.bp)
