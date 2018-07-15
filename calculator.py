# -*- coding: utf-8 -*-
a = float(input())
b = float(input())
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print("Деление на 0!")
    else:
        print(a / b)
elif c == 'mod':
    print(a % b)
elif c == 'div':
    print(a // b)
elif c == 'pow':
    print(a ** b)