from abc import ABC, abstractmethod
from typing import Dict, Union, Type


# Base Shape class
class Shape(ABC):
    @abstractmethod
    def get_details(self) -> Dict[str, Union[str, float]]:
        pass


# Concrete Shape subclasses
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def get_details(self) -> Dict[str, Union[str, float]]:
        return {"shape": "circle", "radius": self.radius}


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def get_details(self) -> Dict[str, Union[str, float]]:
        return {"shape": "square", "side": self.side}


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def get_details(self) -> Dict[str, Union[str, float]]:
        return {"shape": "rectangle", "length": self.length, "width": self.width}


# Factory class
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, *args: float) -> Shape:
        shape_map: Dict[str, Type[Shape]] = {
            "circle": Circle,
            "square": Square,
            "rectangle": Rectangle,
        }

        if shape_type in shape_map:
            return shape_map[shape_type](*args)
        raise ValueError("Unknown shape type")


# Usage examples
circle = ShapeFactory.create_shape("circle", 5)
square = ShapeFactory.create_shape("square", 4)
rectangle = ShapeFactory.create_shape("rectangle", 5, 3)

print(circle.get_details())  # Output: {'shape': 'circle', 'radius': 5}
print(square.get_details())  # Output: {'shape': 'square', 'side': 4}
print(
    rectangle.get_details()
)  # Output: {'shape': 'rectangle', 'length': 5, 'width': 3}
