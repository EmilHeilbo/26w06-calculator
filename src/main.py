from math import pow


def calculate(operator: str, a: float, b: float) -> float:
    match operator:
        case "√":
            return pow(a, (1 / b))
        case "^":
            return pow(a, b)
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            return 0.0


if __name__ == "__main__":
    _ops = ["+", "-", "*", "/", "^", "√"]
    _op = None
    while _op not in _ops:
        _op = input(f"Type your chosen operator of the following: {' '.join(_ops)}\n")
    _num_1 = None
    _num_2 = None
    while None in [_num_1, _num_2]:
        try:
            _num_1 = float(input("Enter the first number: "))
            if _op in _ops[-2:]:
                _num_2 = float(input("Enter the exponent/nth-root: "))
            else:
                _num_2 = float(input("Enter the second number: "))
            _result = calculate(_op, _num_1, _num_2)
            print(_result)
        except ValueError:
            print("The input was not a number, try again.")
    pass
