import logging

import flask_restful
from flask import Flask, jsonify

from api.exception_handlers.invalidusage import BadRequest
from api.resources.health_check import HealthCheck
from api.resources.hotel_recommendations import Recommendation
from api.resources.picklerefresh import PickleRefresh

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE')

api = flask_restful.Api(app)

api.add_resource(Recommendation, '/pricing/recommendation/lodging/', )
api.add_resource(PickleRefresh, '/pricing/recommendation/lodging/model/refresh/', )
api.add_resource(HealthCheck, '/admin/healthcheck/', )

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Catch BadRequest exception globally, serialize into JSON, and respond with 400."""
    payload = dict()
    payload['status'] = error.status
    payload['message'] = error.message
    return jsonify(payload), 400
