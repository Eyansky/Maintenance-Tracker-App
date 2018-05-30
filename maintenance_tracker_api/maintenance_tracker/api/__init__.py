from flask import Flask 

app = Flask(__name__)

from maintenance-tracker.api.tracker.routes import mod

app.register_blueprint(tracker.routes.mod, url_prefix='/api/v1')
