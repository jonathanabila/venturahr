import functools
from decimal import Decimal
from enum import Enum


def factory_boy_decoder(obj_decoder):
    def default(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, Enum):
            return str(obj.value)
        elif isinstance(obj, list):
            return [default(i) for i in obj]

        if hasattr(obj, "__dict__"):
            return {k: default(v) for k, v in obj.__dict__.items() if not k.startswith("_")}
        return obj

    return default(obj_decoder)


def rgetattr(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split("."))


def rsetattr(obj, attr, val):
    pre, _, post = attr.rpartition(".")
    return setattr(rgetattr(obj, pre) if pre else obj, post, val)


def rdelattr(obj, attr):
    pre, _, post = attr.rpartition(".")
    return delattr(rgetattr(obj, pre) if pre else obj, post)
