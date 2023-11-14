#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and height to the same value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square
        Args:
        *args (int): New attribute values
              -1st argument represent id attribute
              -2nd argument represent size attribute
              -3rd argument represent x attribute
              -4th argument represent y attribute
        *kwargs: key/value paired"""
        if args and len(args) != 0:
            idx = 0

            for arg in args:
                if idx == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif idx == 1:
                    self.size = arg
                elif idx == 2:
                    self.x = arg
                elif idx == 3:
                    self.y = arg
                idx += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
