def reverse(string: str) -> str:
    return "".join(reversed(string))

def capital_letters(string: str) -> str:
    return string.upper()

def string_manipulator(func: callable, string: str) -> str:
    return func(string)

if __name__ == "__main__":
    print(string_manipulator(capital_letters, "Hello World!"))
    print(string_manipulator(reverse, "Hello World!"))
    
    