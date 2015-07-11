# -*- coding: utf-8 -*-
"""
simplestruct
===
"""

__version__ = "0.1.0"


class StructMeta(type):

    def __new__(meta, name, bases, dct):
        """Override struct class instantiation so we can store the class
        definition."""
        dct['__struct_meta__'] = dct
        return super(StructMeta, meta).__new__(meta, name, bases, dct)


class Struct(object):
    __metaclass__ = StructMeta

    def __init__(self, **kwargs):
        """Override object constructor to validate the values being set
        first."""
        for attr, val in kwargs.items():
            self._validate_attr(attr, val)
            setattr(self, attr, val)

    def __setattr__(self, attr, val):
        """Override object setter to validate the value being set first."""
        self._validate_attr(attr, val)
        super(Struct, self).__setattr__(attr, val)

    def _validate_attr(self, attr, val):
        """Validates the value being set."""
        if attr not in self.__struct_meta__:
            raise AttributeError(
                "Attribute '%s' is not defined in '%s'" % (attr, self.__class__)
            )

        attr_type = self.__struct_meta__[attr]

        # If the passed value is None, Just let it be.
        if val is None:
            return

        # If the defined attribute is a list, validate each item to match the
        # defined specified attribute type.
        #
        # ie.
        #
        # class Person(Struct):
        #     siblings = [str]
        #
        # Each instance of the attribute `sibling` must be of type `str`.
        #
        if isinstance(attr_type, list):
            if len(attr_type) > 0:
                attr_type = attr_type[0]
                for v in val:
                    if not isinstance(v, attr_type):
                        raise TypeError("")
            return

        # If the defined attribute is a tuple, validate each item in the tuple
        # to match the defined attribute type.
        #
        # ie.
        #
        # class Person(Struct):
        #     age_and_gender = (int, str)
        #
        # The first value of the attribute `age_and_gender` must be of type
        # `int` and the second value must be of type `str`.
        #
        if isinstance(attr_type, tuple):
            for i, v in enumerate(val):
                if v is not None and not isinstance(v, attr_type[i]):
                    raise TypeError("")
            return

        # If the defined attribute is just a type, just validate it.
        #
        # ie.
        #
        # class Person(Struct):
        #     age = int
        #
        # The value of the attribute `age` must be of type `int`.
        if not isinstance(val, attr_type):
            raise TypeError("")
