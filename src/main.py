from math import pow, sqrt


def calculate(operator, num_1, num_2) -> float | AssertionError:
    match operator:
        case "√":
            return num_1 ** (1 / num_2)
        case "^":
            return num_1**num_2
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "*":
            return num_1 * num_2
        case "/":
            return num_1 / num_2
        case _:
            raise AssertionError("The specified operator is incorrect.")


if __name__ == "__main__":
    _operator = input("Type your chosen operator of the following: + - * / ^ √\n")
    _num_1 = float(input("Now enter the first number: "))
    if _operator == "^" or _operator == "√":
        _result = calculate(_operator, _num_1, 2)
        print(_result)
        pass
    _num_2 = float(input("Now enter the second number: "))
    _result = calculate(_operator, _num_1, _num_2)
    print(_result)
    pass
