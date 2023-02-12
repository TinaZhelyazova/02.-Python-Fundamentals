def calculations(operate, number1, number2):
    if operate == "multiply":
        return number1 * number2
    elif operate == "divide":
        return number1 // number2
    elif operate == "add":
        return number1 + number2
    elif operate == "subtract":
        return number1 - number2


operator = input()
num1 = int(input())
num2 = int(input())
print(calculations(operator, num1, num2))
