'''
num1 = float(input("Enter a number with lots of decimal places: ")) #asks a user to input a number that is converted to float
answer = (num1*2)
answer = round(answer, 2)
print(f"Your answer is = {answer}")

import math
num2 = int(input("Enter an integer above 500: "))
answer = round(math.sqrt(num2), 2)
print(f"Your answer is : {answer}")

import math 
answer = round(math.pi, 5)
print(f"Your answer is : {answer}")

import math 
num3 = int(input("Enter a radius of a circle: "))
answer = round(math.pi * (num3 ** 2), 4)
print(f"The area of your circle is {answer}")

import math 
num4 = int(input("Enter a radius of a circle: "))
num5 = int(input("Enter a height of a cylinder: "))
answer = round((math.pi * (num4 ** 2) * num5), 3)
print(f"The area of your circle is {answer}")


num6 = int(input("Enter your first number: "))
num7 = int(input("Enter your second number: "))
answ1 = num6 // num7
answ2 = num6 % num7
print(f"{num6} divided by {num7} is {answ1} with a remainder of {answ2}")
'''

options = int(input("1) Square\n2) Triangle\nEnter a number:"))
if(options == 1):
    length = int(input("Enter the length of a square: "))
    sqArea = length ** 2
    print(f"The area of your square is {sqArea}")
elif(options == 2):
    base = int(input("Enter the base of a triangle: "))
    height = int(input("Enter the heigth of the triangle: "))
    trArea = 0.5 * base * height
    print(f"The area of the triangle is {trArea}")
else:
    print("Enter a number that is either 1 or 2")



