class StringManipulatorStrategy:
    def manipulate_string(self, string: str) -> str:
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
    CAPITLIZE_ME = "Hello World!"
    manipulated_string = ManipulatedString(Capitals())
    print(
        "Manipulated with Capitals:", manipulated_string.manipulate_string(CAPITLIZE_ME)
    )

    # For a larger dataset, you might prefer a different strategy
    REVERSE_ME = "Hello World!"
    manipulated_string = ManipulatedString(Reverse())
    print("Manipulated with Reverse:", manipulated_string.manipulate_string(REVERSE_ME))
