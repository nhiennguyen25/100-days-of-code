import art
print(art.logo)

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# print(operations["+"](2,2))

def calculator():
    first_number = float(input("What's the first number? "))
    new_calculation = True
    while new_calculation:
        for symbol in operations:
            print(symbol)
        choose_operator = input("Pick an operation: ")
        second_number = float(input("What's the next number? "))
        answer = operations[choose_operator](first_number, second_number)
        print(f"{first_number} {choose_operator} {second_number} = {answer}")

        continue_or_restart = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
        if continue_or_restart == "n":
            new_calculation = False
            print("\n" * 20)
            calculator() 

        elif continue_or_restart == "y":
            first_number = answer



calculator()
