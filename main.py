from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

def percent(n1, n2):
    return n1 % n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}


print(logo)

def calculator():
    num_1 = float(input("Enter the first number: \n"))
    for symbol in (operations):
        print(symbol)
    should_continue = True
    while should_continue:
        operation = input("select any operation to continue:\n")
        num_2 = float(input("Enter the second number: \n"))
        calculation_func = operations[operation]
        answer = calculation_func(num_1, num_2)
        print(answer)
        if input("Type 'y' to continue or 'c' to clear the screen:\n").lower() == 'y':
            num_1 = answer
        else:
            should_continue = False
            calculator()
calculator()