'''
for j in range (1,12):
    print (j)

name = input("Enter your name: ")
for i in range(1,4):
    print(name)

name = input("Enter your name: ")
num1 = int(input("Enter a number: "))
for i in range(0, num1):
    print(name)

name = input("Enter your name: ")
for i in name:
    print(i)

name = input("Enter your name: ")
num1 = int(input("Enter a number: "))
for i in range(0, num1):
    for j in name:
        print(j)

num = int(input("Enter a number between 1 and 12: "))
for i in range(1, 13):
    answer = i * num
    print(i, "x", num, "=", answer)

num = int(input("Enter a number between 50: "))
for i in range(50, num-1, -1):
    print(i)

name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    for i in range(0,num):
        print(name)
else:
    for j in range(0,3):
        print("Too high")

total = 0
for i in range(0,5):
    num = int(input("Enter a number: "))
    ans = input("Do you want that number included?(y/n): ")
    if ans == "y":
        total = total + num
print(total)

direction = str.lower(input("Which direction do you want to count?(up/down): "))
if direction == "up":
    top_no = int(input("Enter top_number: "))
    for i in range(1, top_no):
        print(i)
elif direction == "down":
    num = int(input("Enter a number between 20: "))
    for j in range(20, num-1, -1):
        print(j)
else:
    print("I don't understand.")
'''
people = int(input("How many people do you want over for your party? "))
if people < 10:
    for i in range(0, people):
        name = str.lower(input("Enter the name of youe envitee: "))
        print(f"{name} has been invited.")
else:
    print("Too many people.")