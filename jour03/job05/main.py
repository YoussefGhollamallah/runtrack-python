def calcule(num1, operator, num2):

    if operator == "+" :
        return num1 + num2
    elif operator == "*":
        return num1 + num2
    elif operator == "-":
        return num1 + num2
    elif operator == "%":
        return num1 % num2
    elif operator == "/":
        if num2 == 0:
            return "on ne peut pas divisé par Zéro"
        else:
            return num1 / num2
    

print(calcule(50,"%", 2))