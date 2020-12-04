
#Ask for two numbers. If the first one is larger than the second, 
# display the second number first and then the first number, 
#otherwise show the first number first and then the second.
num1 = int(input("Enter your first-number: "))
num2 = int(input("Enter your second-number: "))
if num1 > num2:
    print(f'Your smaller number is {num2} \nYour larger number is {num1}')
else:
    print(f'Your smaller number is {num1} \nYour larger number is {num2}')

#Ask the user to enter a number that is under 20. 
# If they enter a number that is 20 or more, 
# display the message “Too high”, otherwise display “Thank you”.
num = int(input("Enter a number under 20: "))
if num >= 20:
    print("Too high.")
else:
    print("Thank you.")
#Ask the user to enter a number between 10 and 20 (inclusive). 
#If they enter a number within this range,
# display the message “Thank you”, otherwise display the message “Incorrect answer”.
num = int(input("Enter a number between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank you.")
else:
    print("Incorrect answer.")

#Ask the user to enter their favourite colour. If they enter “red”, “RED” or
#“Red” display the message “I like red too”, otherwise display the message
#“I don’t like [colour], I prefer red”
color = str(input("Enter your favourite color: "))
if color == "red" or color == "Red" or color == "RED":
    print("I like red too.")
else:
    print(f"I don't like {color}, I prefer red.")

'''
Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”.
'''

que1 = str.lower(input("Is it raining? "))
if que1 == "yes":
    que2 = str.lower(input("Is it windy? "))
    if que2 == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day.")

'''
Ask the user’s age. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trick-
or-Treating”.
'''

age = int(input("Enter your age: "))
if age >= 18 :
    print("You can Vote.")
elif age == 17:
    print("You can learn to drive.")
elif age == 16:
    print("You can buy a lottery ticket.")
else age < 16:
    print("You can go Trick or Treating.")
'''
Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”.
'''
num = int(input("Enter a number: "))
if num < 10:
    print("Too low.")
elif num >= 10 and num <= 20:
    print("correct")
else:
    print("Too High.")

'''
Ask the user to enter 1, 2 or 3. If they enter a 1, display
the message “Thank you”, if they enter a 2, display
“Well done”, if they enter a 3, display “Correct”. If
they enter anything else, display “Error message”.
'''
num = int(input("Enter either 1,2 or 3: "))
if num == 1:
    print("Thank You")
elif num == 2:
    print("Well done")
elif num == 3:
    print("correct")
else:
    print("Error message")