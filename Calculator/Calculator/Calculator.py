from pickle import FALSE
from art import logo
print(logo)

print("Welcome to Calculator  \n")

#Add
def add(number1, number2):
    return number1 + number2

#Subtract
def sub(number1, number2):
    return number1 - number2

#Multiply
def multiply(number1, number2):
    return number1 * number2

#Divide
def divied(number1, number2):
    return number1 / number2


operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divied,
}

should_continue = True
while should_continue:
    num1 = float(input("What's the first number? "))

    for key in operations:
        print(key)
    
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    should_continue = input("Type 'y' to continue calculating or type 'n' to exit.: ")
    if should_continue == 'n':
        should_continue = False    