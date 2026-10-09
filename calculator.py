
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def modulus(a, b):
    return a % b


while True:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nSelect Operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    print("% for Modulus")

    operation = input("Enter operation: ")

    if operation == "+":
        result = addition(num1, num2)

    elif operation == "-":
        result = subtraction(num1, num2)

    elif operation == "*":
        result = multiplication(num1, num2)

    elif operation == "/":
        if num2 != 0:
            result = division(num1, num2)
        else:
            print("Error! Division by zero is not allowed.")
            result = None

    elif operation == "%":
        if num2 != 0:
            result = modulus(num1, num2)
        else:
            print("Error! Modulus by zero is not allowed.")
            result = None

    else:
        print("Invalid operation!")
        result = None

    if result is not None:
        print("Result =", result)

    choice = input("\nDo you want another calculation? (yes/no): ")

    if choice.lower() != "yes":
        print("Calculator closed.")
        break

