#!/usr/bin/python3
"""
class called BaseGeometry
"""


class BaseGeometry:
    """
    class called BaseGeometry
    """
    try:
        def area(self):
            """area() is not implemented"""
            raise Exception("area() is not implemented")
        pass
    except Exception as e:
        pass

    def integer_validator(self, name, value):
        """integer_validator() is not implemented"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class called Rectangle
    attributes:
        width: integer
        height: integer
    methods:
        __init__(self, width, height)
        area(self)
        integer_validator(self, name, value)
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
