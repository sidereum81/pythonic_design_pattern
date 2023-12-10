from typing import List, Callable, TypeVar, Generic

T = TypeVar('T')

class Pipeline:
    def __init__(self):
        self.pipes : List = []

    def add_pipe(self, pipe: Callable[[T], T]) -> 'Pipeline[T]':
        self.pipes.append(pipe)
        return self

    def process(self, data: T) -> T:
        for pipe in self.pipes:
            data = pipe(data)

        return data

def capital_letters(string: str) -> str:
    return string.upper()

def reverse(string: str) -> str:
    return "".join(reversed(string))


if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.add_pipe(capital_letters).add_pipe(reverse)
    result = pipeline.process("Hello world!")
    print(result)