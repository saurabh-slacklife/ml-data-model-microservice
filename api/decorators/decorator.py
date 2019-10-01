from marshmallow import ValidationError
from functools import wraps
import math


def validator_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)

    return wrapper


def check_positive(func):
    @wraps(func)
    def func_wrapper(value):
        if value < 0:
            raise Exception("The field should be positive")
        res = func(value)
        return res
    return func_wrapper


def validate_string(func):
    @wraps(func)
    def func_wrapper(value):
        if value is None:
            raise ValidationError("The field should not be None")
        res = func(value)
        return res
    return func_wrapper

def validateNan(func):
    @wraps(func)
    def func_wrapper(value):
        if math.isnan(value):
            raise ValidationError("The field should not be None")
        res = func(value)
        return res
    return func_wrapper
