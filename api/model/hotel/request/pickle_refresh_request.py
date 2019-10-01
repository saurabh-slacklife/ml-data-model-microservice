import logging

from marshmallow import Schema, fields, post_load


class PickleRefreshRequest():
    def __init__(self, path):
        self.path = path

class PickleRefreshRequestSchema(Schema):
    path = fields.Str(required=True)

    __logger = logging.getLogger('gunicorn.error')

    @post_load
    def request_schema(self, data):
        return PickleRefreshRequest(**data)