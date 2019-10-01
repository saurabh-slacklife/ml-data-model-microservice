from api.common.pickle_singleton_loader import PickleLoader
from api.common.utils import create_pr_recommendation_response
import logging
from api.model.hotel.response.hotel_response import HotelResponse

class prediction_crystall_ball():
    __logger = logging.getLogger('gunicorn.error')

    def crystall_ball_prediction(self, query):
        pickle_loader = PickleLoader.getInstance()
        crystallball = pickle_loader.crystallball

        hotel_ds_response = self.__parse_crystall_ball_response(crystallball.forecast(query))
        self.__logger.info('Response received from model query: %s', query)
        hotel_response = HotelResponse(hotel_ds_response)

        return hotel_response

    def __parse_crystall_ball_response(self, ds_response):
        return create_pr_recommendation_response(ds_response)
