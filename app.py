from routes import auth, index
from routes.api import user, repo
from flask import Flask

app = Flask(__name__)
app.register_blueprint(index.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(user.bp)
app.register_blueprint(repo.bp)
