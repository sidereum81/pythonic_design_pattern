from typing import Protocol, TypeVar, Generic, Dict, Type
from dataclasses import dataclass

# Define a protocol for the manipulator
class Manipulator(Protocol):
    def manipulate(self, string: str) -> str:
        ...

# Implementing the protocol with different classes
class Reverser:
    def manipulate(self, string: str) -> str:
        return "".join(reversed(string))

class Capitalizer:
    def manipulate(self, string: str) -> str:
        return string.upper()

# Define a type variable for the generic class
T = TypeVar('T', bound=Manipulator)

# Annotate StringManipulator as a generic class
@dataclass
class StringManipulator(Generic[T]):
    manipulator: T

    def manipulate(self, string: str) -> str:
        return self.manipulator.manipulate(string)

# Usage
print(StringManipulator(Reverser()).manipulate("hello"))
print(StringManipulator(Capitalizer()).manipulate("hello"))

# Dictionary with manipulator classes and strings
manipulations: Dict[Type[Manipulator], str] = {
    Reverser: "hello",
    Capitalizer: "world",
}

# Applying the manipulations in order
for manipulator_class, text in manipulations.items():
    print(StringManipulator(manipulator_class()).manipulate(text))