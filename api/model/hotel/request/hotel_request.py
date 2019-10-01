import logging

from marshmallow import Schema, fields, post_load, validates, ValidationError

from api.model.hotel.request.itinerary import ItineraryRequestSchema


class HotelPrRequest():
    def __init__(self, hotelId, itinerary):
        self.hotelId = hotelId
        self.itinerary = itinerary

class HotelPrRequestSchema(Schema):

    hotelId = fields.Function(lambda obj: obj, required=True)
    itinerary = fields.Nested(ItineraryRequestSchema, many=True)

    __logger = logging.getLogger('gunicorn.error')

    class Meta:
        # Fields to expose
        fields = ('hotelId', 'itinerary')

    @post_load
    def request_schema(self, data):
        return HotelPrRequest(**data)

    @validates('hotelId')
    def validate_hotel_id(self, value):
        if not (isinstance(value, int) or isinstance(value, long)):
            self.__logger.error('Invalid Hotel Id: %s', value)
            raise ValidationError("Invalid Hotel Id: %s" % value)
        elif value < 0:
            self.__logger.error('Invalid Hotel Id: %s',  value)
            raise ValidationError("Invalid Hotel Id: %s" % value)

class HotelRequest():
    def __init__(self, hotelPrRequest):
        self.hotelPrRequest = hotelPrRequest

class HotelRequestSchema(Schema):
    hotelPrRequest = fields.Nested(HotelPrRequestSchema, many=True)

    class Meta:
        class Meta:
            # Fields to expose
            fields = ('hotelPrRequest')

    @post_load
    def request_schema(self, data):
        return HotelRequest(**data)

