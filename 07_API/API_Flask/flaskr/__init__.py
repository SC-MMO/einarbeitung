import os
from flask import Flask, jsonify, abort
from logging.config import dictConfig
from .db import read_tables, read_rows

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

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    @app.route('/api/<table>', methods=['GET'])
    def return_all_objects(table):
        if table not in [table[0] for table in read_tables()]:
            abort(404, description="Table not found")
        
        rows = read_rows(table=table)
        
        if not rows:
            abort(404, description="Table was empty, no objects exist")
        
        return jsonify(rows)

    @app.route('/api/<table>/<int:id>', methods=['GET'])
    def return_one_object(table, id):
        if table not in [table[0] for table in read_tables()]:
            abort(404, description="Table not found")
        
        rows = read_rows(table=table, limit=1, filter_args=[f'{table[:-1]}Id = {id}'])
        
        if not rows:
            abort(404, description="Object not found")
        
        return jsonify(rows[0])

    return app