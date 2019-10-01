from marshmallow import Schema, fields, post_load
from api.model.hotel.response.recommendation import HotelPrRecommendationSchema


class HotelPrResponse():
    def __init__(self, id, startDay, recommendation):
        self.hotelId = id
        self.stayDate = startDay
        self.recommendations = recommendation

class HotelPrResponseSchema(Schema):
    hotelId = fields.Integer()
    stayDate = fields.Str()
    recommendations = fields.Nested(HotelPrRecommendationSchema, many=True)

    class Meta:
        class Meta:
            fields = ('hotelId', 'stayDate', 'recommendations')

    @post_load
    def request_schema(self, data):
        return HotelPrResponse(**data)

class HotelResponse():
    def __init__(self, hotel_pr_response):
        self.hotels = hotel_pr_response