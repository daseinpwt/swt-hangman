from importlib import import_module
from .base import BaseWordGenerator

def get(word_name, *args, **kwargs):
    try:
        if '.' in word_name:
            module_name, class_name = word_name.rsplit('.', 1)
        else:
            module_name = word_name
            class_name = word_name.capitalize()

        word_module = import_module('.' + module_name, package="wordgenerator")

        word_class = getattr(word_module, class_name)

        instance = word_class(*args, **kwargs)

    except (AttributeError, ModuleNotFoundError):
        raise ImportError('The word generator you tried to use is not part of our word generator collection!')
    else:
        if not issubclass(word_class, BaseWordGenerator):
            raise ImportError("We currently have not implemented {}".format(word_class))

    return instance
