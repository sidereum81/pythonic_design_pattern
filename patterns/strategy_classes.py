from typing import List


class StringManipulatorStrategy:
    def mainipulate_string(self, data: List[int]) -> List[int]:
        raise NotImplementedError


class Reverse(StringManipulatorStrategy):
    def manipulate_string(self, string: str) -> str:
        # Implement reverse
        return "".join(reversed(string))  # Simplified for demonstration


class Capitals(StringManipulatorStrategy):
    def manipulate_string(self, string: str) -> str:
        # Implement upper here
        return string.upper()  # Simplified for demonstration


class ManipulatedString:
    def __init__(self, strategy: StringManipulatorStrategy):
        self._strategy = strategy

    def manipulate_string(self, string: str) -> str:
        return self._strategy.manipulate_string(string)


if __name__ == "__main__":
    # Small dataset
    string = "Hello World!"
    manipulated_string = ManipulatedString(Capitals())
    print("Manipulated with Capitals:", manipulated_string.manipulate_string(string))

    # For a larger dataset, you might prefer a different strategy
    string = "Hello World!"
    manipulated_string = ManipulatedString(Reverse())
    print("Manipulated with Reverse:", manipulated_string.manipulate_string(string))
