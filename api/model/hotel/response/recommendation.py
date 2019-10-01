from marshmallow import Schema, fields, post_load, validates, ValidationError


class HotelPrRecommendation:
    def __init__(self, los, opaque_rate, opaque_vol, recommended_rate, retail_rate_mod, room_night_opportunity,
                 winner_rate, winner_vol):
        self.los = los
        self.opaqueRate = opaque_rate
        self.opaqueVol = opaque_vol
        self.recommendedRate = recommended_rate
        self.retailRateMod = retail_rate_mod
        self.roomNightOpportunity = room_night_opportunity
        self.winnerRate = winner_rate
        self.winnerVol = winner_vol


class HotelPrRecommendationSchema(Schema):
    los = fields.Integer(required=True)
    opaqueRate = fields.Float(required=True)
    opaqueVol = fields.Float(required=True)
    recommendedRate = fields.Float(required=True)
    retailRateMod = fields.Float(required=True)
    roomNightOpportunity = fields.Float(required=True)
    winnerRate = fields.Float(required=True)
    winnerVol = fields.Float(required=True)

    class Meta:
        class Meta:
            fields = (
            'los', 'opaqueRate', 'opaqueVol', 'recommendedRate', 'retailRateMod', 'roomNightOpportunity', 'winnerRate',
            'winnerVol')

    @post_load
    def request_schema(self, data):
        return HotelPrRecommendation(**data)
