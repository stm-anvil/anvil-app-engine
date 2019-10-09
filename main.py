#!/usr/bin/env python3
import logging
from datetime import datetime

from flask import Flask
import anvil.server
from anvil.tables import app_tables


anvil.server.connect('PUT YOUR UPLINK KEY HERE')
app = Flask(__name__)


@app.route('/logme/<name>')
def log_name(name):
    """Log the request path in a Data Table."""
    app_tables.name_log.add_row(name=name, when=datetime.now())
    result = anvil.server.call('log_the_name', name)
    return result


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)


