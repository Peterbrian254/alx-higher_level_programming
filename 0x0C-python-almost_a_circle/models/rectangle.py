#!/usr/bin/python3
"""rectangle module defines a class Rectangle with private
instance attributes width, height, x, y and methods area,
display
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        for k, v in {"width": width, "height": height, "x": x, "y": y}.items():
            self.validate_int(k, v)
        for k, v in {"width": width, "height": height}.items():
            self.validate_width_and_height(k, v)
        for k, v in {"x": x, "y": y}.items():
            self.validate_x_and_y(k, v)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.validate_int("width", value)
        self.validate_width_and_height("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.validate_int("height", value)
        self.validate_width_and_height("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.validate_x_and_y("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.validate_x_and_y("y", value)
        self.__y = value

    def area(self):
        """Returns the area of a rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        """prints the rectangle instance with the
        character #
        """
        for j in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".\
           format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
            args: list of attribute values to assign
            kwargs: dictionary of attributes to assign
        """
        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            i = len(args)
            idx = 0
            while i:
                setattr(self, attrs[idx], args[idx])
                idx += 1
                i -= 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"id": self.id,
                "height": self.height,
                "width": self.width,
                "x": self.x,
                "y": self.y}

    @classmethod
    def validate_int(self, attribute, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))

    @classmethod
    def validate_width_and_height(self, attribute, value):
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    @classmethod
    def validate_x_and_y(self, attribute, value):
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))
