num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))
operator = input("Please enter an operator: +, -, *, /: ")

def add(num1, num2, operator):
    description = f"{num1} {operator} {num2}"
    if operator == "+":
        description = num1 + num2
    elif operator == "-":
        description = num1 - num2
    elif operator == "*":
        description = num1 * num2
    elif operator == "/":
        description = num1 / num2
    return f"The result of the calculation is {description}"

print(add(num1, num2, operator))
