from flask_restful import Resource

from api.common.constants import HTTP_HEADER, HTTP_STATUS
from api.common.utils import CustomJsonEncoder


class HealthCheck(Resource):
    def get(self):
        from api.app import app
        response = {
            'status': 'Success',
            'message': 'The Service is Healthy'
        }
        response = app.response_class(
            response=CustomJsonEncoder().encode(response),
            status=HTTP_STATUS.HTTP_OK.value,
            mimetype=HTTP_HEADER.MIME_TYPE_JSON.value
        )
        return response