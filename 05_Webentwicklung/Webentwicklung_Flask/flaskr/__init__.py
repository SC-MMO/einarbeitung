import os
from flask import Flask, redirect, url_for, render_template, abort, session, g, request
from logging.config import dictConfig

def create_app(test_config=None):
    # create and configure the app
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
    
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .members import member_bp
    app.register_blueprint(member_bp)
    from .squads import squad_bp
    app.register_blueprint(squad_bp)
    
    @app.route('/', methods=["GET", "POST"])
    def index():
        return render_template("base.html")

    return app