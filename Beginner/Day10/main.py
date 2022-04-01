import art

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print(art.logo)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
continue_calc = True
use_result = "n"
first_number = 0

while continue_calc:
    if use_result == "n":
        first_number = float(input("What's the first number? "))
    for op in operations:
        print(op)
    operation_input = input("Pick an operation: ")
    second_number = float(input("What's the next number? "))
    operation = operations[operation_input]
    result = operation(first_number, second_number)
    print(f"{first_number} {operation_input} {second_number} = {result}")

    use_result = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation"
                       f"or type 'exit' to end the program: ")
    if use_result == "exit":
        continue_calc = False
    elif use_result == "y":
        first_number = result

