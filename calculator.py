def calculate(first_number, operation, second_number):
    if operation == "+":
        return first_number + second_number
    if operation == "-":
        return first_number - second_number
    if operation == "*":
        return first_number * second_number
    if operation == "/":
        if second_number == 0:
            return "Cannot divide by zero"
        return first_number / second_number
    return "Invalid operation"


def main():
    try:
        first_number = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        second_number = float(input("Enter the second number: "))
        result = calculate(first_number, operation, second_number)
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers")


if __name__ == "__main__":
    main()
