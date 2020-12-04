
#challenge1
#ask the user FirstName and display the output message as
#hello[FirstName]
F_Nam= input("Enter your FirstName: ")
#challenge2
#ask fo the firstname and the surname and print output
#hello[firstname][surname]
S_Nam = input("Enter your Surname: ")
print("Hello!!!  " + F_Nam + S_Nam)

#code that will display the joke “What do you call a bear with no teeth?” 
# and on the next line display the answer “A gummy bear!” Try to create it using only one line of code.
print("What do you call a bear with no teeth?\nA gummy bear!")

#Ask the user to enter two numbers. Add them together and display the answer as
#the total is [answer]
num1 = int(input("Enter firstnumber: "))
num2 = int(input("Enter secondnumber: "))
#Ask the user to enter three numbers. Add together the first two numbers 
# and then multiply this total by the third. Display the answer as The answer is [answer]
total = num1 + num2
num3 = int(input("Enter a thirdnumber: "))
answer = total * num3
print("The answer is:", answer)


#Ask how many slices of pizza the user started with 
# and ask how many slices they have eaten.
#Work out how many slices they have left
#display the answer in a user friendly format.
slices_ordered = int(input("How many pizza slices did you start with? "))
slices_ate = int(input("How many have you eaten so far? "))
slices_left = (slices_ordered - slices_ate)
print("You have {} slices left".format(slices_left))
#Ask the user for their name and their age. 
# Add 1 to their age and display the output [Name] next birthday you will be [new age] .
Name = str(input("Enter your Name: "))
age = int(input("Enter your age: "))
new_age = age + 1
print(f"{Name} next birthday you will be {new_age}")


#Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the
#number of diners and show how much each person must pay
total_price = int(input("What's the total price for the bill: "))
dinners = int(input("How many dinners are there? "))
bill = total_price/dinners
print(f'Each person is supposed to pay: {bill}')
#Write a program that will ask for a number of days and then will show how many hours, minutes 
# and seconds are in that number of days.
days = int(input("How many days: "))
hours = (days*24)
minutes = (hours*60)
seconds = (minutes*60)
print(f'The {days} days you have entered has {hours} hours, {minutes} minutes and {seconds} seconds.')
#There are 2,204 pounds in a kilogram. 
# Ask the user to enter a weight in kilograms and convert it to pounds.
weight = int(input("Enter your weight in Kilograms: "))
pounds = weight*2204
print(f'Your weight in pounds is {pounds}.')

#There are 2,204 pounds in a kilogram. 
# Ask the user to enter a weight in kilograms and convert it to pounds.
num1 = int(input("Enter a number above 100: "))
num2 = int(input("Enter a number below 10: "))
answer = num1//num2
print(f'{num2} goes into {num1}, {answer} times.')