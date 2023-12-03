from typing import Callable, Dict, Union


def create_circle(radius: int):
    return {"shape": "circle", "radius": radius}


def create_square(side: int):
    return {"shape": "square", "side": side}


def create_rectangle(length: int, width: int):
    return {"shape": "rectangle", "length": length, "width": width}


# Define the type for the shape creation functions
ShapeCreator = Callable[..., Dict[str, Union[str, float]]]

shape_factory: Dict[str, ShapeCreator] = {
    "circle": create_circle,
    "square": create_square,
    "rectangle": create_rectangle,
}


def create_shape(shape_type: str, *args: Union[int, int]):
    if shape_type in shape_factory:
        return shape_factory[shape_type](*args)
    raise ValueError("Unknown shape type")


# Usage examples
circle = create_shape("circle", 5)
square = create_shape("square", 4)
rectangle = create_shape("rectangle", 5, 3)

print(circle)  # Output: {'shape': 'circle', 'radius': 5}
print(square)  # Output: {'shape': 'square', 'side': 4}
print(rectangle)  # Output: {'shape': 'rectangle', 'length': 5, 'width': 3}
