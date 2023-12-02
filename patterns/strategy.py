def reverse(string: str) -> str:
    return "".join(reversed(string))

def capital_letters(string: str) -> str:
    return string.upper()

def strategy(func: callable, string: str) -> str:
    return func(string)

if __name__ == "__main__":
    print(strategy(capital_letters, "Kenneth"))
    print(strategy(reverse, "Kenneth"))