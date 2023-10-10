import functools


def singleton(class_):
    instances = {}

    @functools.wraps(class_)
    def getinstance(*args, **kwargs):
        key = (class_, tuple(args), frozenset(kwargs.items()))

        if key not in instances:
            instances[key] = class_(*args, **kwargs)
        return instances[key]

    return getinstance
