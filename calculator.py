op = input("enter an operator: * + - /")
num1 = float(input('input first number: '))
num2 = float(input('input second number: '))

if op == '+':
    print(num1 + num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
else:
    print('Invalid input')