#Ask the user to enter their first name and then display the length of their name.
name = str(input("Enter your first-name: "))
print(f'Your name has {len(name)} characters.')

"""
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.
"""
f_name = str(input("Enter your first_name: "))
s_name = str(input("Enter your surname: "))
name = f_name + " " + s_name
print(f'Your name is {name} and it has {len(name)} characters')

"""
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.
"""
f_name = str.lower(input("Enter your firstname: "))
s_name = str.lower(input("Enter your surname: "))
name = f_name + " " + s_name
print(name.title())
"""
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1).
"""
line = str(input("Type in your first line of a nursery rhyme: "))
print(f'Your line has {len(line)} characters')
s_num = int(input("Enter your starting number: "))
e_num = int(input("Enter your ending number: "))
print(f'Your new line is "{line[s_num:e_num]}"')
"""
Ask the user to type in any word and display it in
upper case.
"""
text = str(input("Enter any word: "))
print(text.upper())
"""
Ask the user to enter their first name. If the length
of their first name is under five characters, ask
them to enter their surname and join them
together (without a space) and display the name
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case.
"""
f_name = str(input("Enter your firstname: "))
if len(f_name) < 5:
    s_name =str(input("Enter your surname: "))
    name = f_name + " " + s_name
    print(name.upper())
else:
    print(f_name.lower())