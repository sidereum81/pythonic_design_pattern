from typing import Callable, Iterable

# Note, example from ArjanCodes episode: https://www.youtube.com/watch?v=3iJjBOne2sM

def validate_pipeline(validators: Iterable[Callable[[int],bool]]) -> Callable[[int],bool]:
    def validator(value: int) -> bool:
        return all(validator(value) for validator in validators)

def is_even(value: int) -> bool:
    return value % 2 == 0

def is_positive(value: int) -> bool:
    return value > 0


def main() -> None:
    validator = validate_pipeline([is_even, is_positive])
    result = validator(4)
