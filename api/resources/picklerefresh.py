import logging

from flask import request
from flask_restful import Resource

from api.common.constants import HTTP_HEADER, HTTP_STATUS
from api.common.pickle_singleton_loader import PickleLoader
from api.common.utils import parse_pickle_refresh_request


class PickleRefresh(Resource):
    __logger = logging.getLogger('gunicorn.error')

    def get(self):
        from api.app import app
        self.__logger.info('Call received for Model refresh')
        PickleLoader.getInstance().refresh_pickle(app.config['AWS_S3_PATH'])
        self.__logger.info('Call ended for Model refresh')
        response = app.response_class(
            status=HTTP_STATUS.HTTP_OK.value,
            mimetype=HTTP_HEADER.MIME_TYPE_JSON.value
        )
        return response

    def post(self):
        from api.app import app
        pickle_path = request.get_json()
        request_path = parse_pickle_refresh_request(pickle_path)
        self.__logger.info('Call ended for Model refresh=%s', request_path.path)
        PickleLoader.getInstance().refresh_pickle_from_s3_aws(request_path.path)
        response = app.response_class(
            status=HTTP_STATUS.HTTP_OK.value,
            mimetype=HTTP_HEADER.MIME_TYPE_JSON.value
        )
        return response
