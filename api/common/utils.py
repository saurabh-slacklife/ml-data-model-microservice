import pickle
from collections import defaultdict
from io import BytesIO
from json import JSONEncoder

import boto3
import logging
from marshmallow import ValidationError

from api.decorators.decorator import validate_string, validateNan
from api.exception_handlers.invalidusage import BadRequest
from api.model.hotel.request.hotel_request import HotelRequestSchema
from api.model.hotel.response.hotel_response import HotelPrResponse
from api.model.hotel.response.recommendation import HotelPrRecommendation
from api.model.hotel.request.pickle_refresh_request import PickleRefreshRequestSchema
from api.common.constants import HTTP_STATUS

__logger = logging.getLogger('gunicorn.error')


def parse_hotelPr_request(request):
    try:
        hotel_pr_request_object_list = None
        hotel_pr_request, errors = HotelRequestSchema().load(request)
        if errors:
            __logger.error('Unable to parse request for HotelId: %s', request)
            raise BadRequest(message=errors, status=HTTP_STATUS.HTTP_BAD_REQUEST.value)
        if hotel_pr_request:
            hotel_pr_request_object_list = hotel_pr_request.hotelPrRequest
        return hotel_pr_request_object_list
    except BadRequest as err:
        raise err
    except ValidationError as err:
        raise err


def parse_pickle_refresh_request(request):
    try:
        pickle_refresh_request, errors = PickleRefreshRequestSchema().load(request)
        if errors:
            __logger.error('Unable to parse request: %s', request)
            raise BadRequest(message=errors, status=HTTP_STATUS.HTTP_BAD_REQUEST.value)
        return pickle_refresh_request
    except ValidationError as err:
        raise err

def create_pr_recommendation_response(ds_response):
    hotelid_stay_code_dict = defaultdict(list)
    hotel_recommend_dict = defaultdict(list)
    for hotel_recommendation in ds_response:
        __logger.info('The complete response was: %s', hotel_recommendation)
        try:
            validateNanValue(hotel_recommendation['hotelPrice'])
            validateNanValue(hotel_recommendation['hotelPriceProd'])
            validateNanValue(hotel_recommendation['recommendedPrice'])
            validateNanValue(hotel_recommendation['recommendedPriceProd'])
            validateNanValue(hotel_recommendation['winnerPrice'])
            validateNanValue(hotel_recommendation['winnerPriceProd'])

            hotelPr_recommendation = HotelPrRecommendation(los=hotel_recommendation['los'],
                                                           opaque_rate=hotel_recommendation['hotelPrice'],
                                                           opaque_vol=hotel_recommendation['hotelPriceProd'],
                                                           recommended_rate=hotel_recommendation['recommendedPrice'],
                                                           retail_rate_mod=None,
                                                           room_night_opportunity=hotel_recommendation['recommendedPriceProd'],
                                                           winner_rate=hotel_recommendation['winnerPrice'],
                                                           winner_vol=hotel_recommendation['winnerPriceProd'])
            hotelid_stay_code_dict[hotel_recommendation['hotelID']].append(hotel_recommendation['date'])

            hotel_recommend_dict[
                str(int(float(hotel_recommendation['hotelID']))) + '~' + hotel_recommendation['date']].append(
                hotelPr_recommendation)

            __logger.info('The Passed response was: %s', hotel_recommendation)
        except ValidationError as err:
            __logger.error('Unable to parse Data Science response for HotelId: %s, Start-Day-Code: %s and LOS: %s',
                           hotel_recommendation['hotelID'], hotel_recommendation['date'], hotel_recommendation['los'])
            __logger.error('The Failed response was: %s', hotel_recommendation)
            __logger.error(err)

    response_list = []

    if hotel_recommend_dict.keys().__len__() == 0:
        return response_list


    for key, value in hotel_recommend_dict.items():
        key_split_values = key.split('~')
        hotelId = key_split_values[0]
        startDay = key_split_values[1]
        hotel_pr_response = HotelPrResponse(id=hotelId, startDay=startDay,
                                         recommendation=value)
        response_list.append(hotel_pr_response)
    return response_list

def create_request_for_ds_prediction(request):
    hotel_ds_request_list = []
    for hotel_request in request:
        __logger.info('Request received for HotelId: %s', hotel_request.hotelId)
        for itinerary in hotel_request.itinerary:
            hotel_ds_request = {}
            hotel_ds_request['los'] = itinerary.los
            hotel_ds_request['hotel_id'] = hotel_request.hotelId
            hotel_ds_request['start_day_code'] = itinerary.date
            hotel_ds_request['query_price'] = itinerary.hotelPrice
            hotel_ds_request_list.append(hotel_ds_request)
    return hotel_ds_request_list

def load_pickle_from_s3(path):
    from api.app import app
    bucket = app.config['AWS_S3_BUCKET']
    crystallball = None
    s3_resource = boto3.resource('s3')
    __logger.info('Trying to load pickle from: %s', bucket+path)
    with BytesIO() as data:
        s3_resource.Bucket(bucket).download_fileobj(path, data)
        data.seek(0)
        crystallball = pickle.load(data)
    return  crystallball

@validate_string
@validateNan
def validateNanValue(data):
    pass



class CustomJsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
