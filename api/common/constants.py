from enum import Enum

class HTTP_STATUS(Enum):
    HTTP_OK = 200
    HTTP_RECEIVED = 201
    HTTP_ACCEPTED = 202
    HTTP_NO_CONTENT = 204
    HTTP_BAD_REQUEST = 400

class HTTP_HEADER(Enum):
    MIME_TYPE_JSON = 'application/json'