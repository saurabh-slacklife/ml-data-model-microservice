import logging

from flask import request
from flask_restful import Resource

from api.common.constants import HTTP_STATUS, HTTP_HEADER
from api.common.crsytal_ball_prediction import prediction_crystall_ball
from api.common.utils import CustomJsonEncoder
from api.common.utils import create_request_for_ds_prediction
from api.common.utils import parse_hotelPr_request


class Recommendation(Resource):
    __logger = logging.getLogger('gunicorn.error')

    def post(self):
        from api.app import app

        hotel_request_json = request.get_json()
        hotel_pr_request_object_list = parse_hotelPr_request(hotel_request_json)

        input_query = create_request_for_ds_prediction(hotel_pr_request_object_list)
        response_recommendation_list = prediction_crystall_ball().crystall_ball_prediction(input_query)

        if response_recommendation_list is None or response_recommendation_list.hotels is None or response_recommendation_list.hotels.__len__() < 1:

            self.__logger.warn('No Response received from model: %s', input_query)

            response = app.response_class(
                response=CustomJsonEncoder().encode(response_recommendation_list),
                status=HTTP_STATUS.HTTP_NO_CONTENT.value,
                mimetype=HTTP_HEADER.MIME_TYPE_JSON.value
            )
        else:
            self.__logger.info('Total Prediction count received: %s', response_recommendation_list.hotels.__len__())
            response = app.response_class(
                response=CustomJsonEncoder().encode(response_recommendation_list),
                status=HTTP_STATUS.HTTP_OK.value,
                mimetype=HTTP_HEADER.MIME_TYPE_JSON.value
            )

        return response
