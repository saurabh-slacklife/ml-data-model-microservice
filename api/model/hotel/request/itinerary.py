from marshmallow import Schema, fields, post_load, pre_dump, validates, ValidationError
from datetime import datetime
import logging


class ItineraryRequest(object):
    def __init__(self, date, los, hotelPrice, winnerPrice, currency):
        self.date = date
        self.los = los
        self.hotelPrice = hotelPrice
        self.winnerPrice = winnerPrice
        self.currency = currency


class ItineraryRequestSchema(Schema):
    date = fields.Str(required=True)
    los = fields.Function(lambda obj: obj, required=True)
    hotelPrice = fields.Float(required=True)
    winnerPrice = fields.Float()
    currency = fields.Str(required=True)

    __logger = logging.getLogger('gunicorn.error')

    class Meta:
        # Fields to expose
        fields = ('date', 'los', 'hotelPrice', 'winnerPrice', 'currency')

    @post_load
    def request_itinerary_schema(self, data):
        return ItineraryRequest(**data)

    @validates('date')
    def validate_date(self, date_value):
        try:
            request_date = datetime.strptime(date_value, '%Y-%m-%d')
            current_date = datetime.utcnow()
            diff = current_date - request_date
            if diff.days > 0:
                self.__logger.error('Date passed cannot be old date: %s', date_value)
                raise ValidationError("Date passed cannot be old 'date: %s'" % date_value)
        except ValueError:
            self.__logger.error('Incorrect data format for field date: %s, should be YYYY-MM-DD', date_value)
            raise ValidationError("Incorrect data format for field 'date: %s', should be YYYY-MM-DD" % date_value)

    @validates('los')
    def validate_los(self, los):
        if not (isinstance(los, int)):
            self.__logger.error('Invalid los: %s', los)
            raise ValidationError('Invalid los: %s', los)
        elif los <= 0:
            self.__logger.error('los should be positive integer: %s', los)
            raise ValidationError("los should be positive integer: %s" % los)

    @validates('hotelPrice')
    def validate_hotel_price(self, hotel_price):
        if hotel_price <= 0:
            self.__logger.error('Hotel Price should be greater than 0.0: %s', hotel_price)
            raise ValidationError("Hotel Price should be greater than 0.0: %s" % hotel_price)
