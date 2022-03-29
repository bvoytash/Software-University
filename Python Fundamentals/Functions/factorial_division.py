

def factorial(num1, num2):
    num1_factorial = num1
    num2_factorial = num2
    for i in range(num1 - 1, 0, -1):
        num1_factorial = num1_factorial * i

    for y in range(num2 - 1, 0, -1):
        num2_factorial = num2_factorial * y

    return (f"{(num1_factorial / num2_factorial):.2f}")


number1 = int(input())
number2 = int(input())

print(factorial(number1, number2))