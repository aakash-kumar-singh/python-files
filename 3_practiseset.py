# Problem 1
name = input("Enter your name\n")
print("Good afternoon\t" + name)
# problem 2
letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards.
Date: <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)
# Problem 3
st = "This is a string with double  spaces"
doublespaces = st.find("  ")
print(doublespaces)
# Problem 4
mt = "This is a string with double  spaces  ok"
mt = mt.replace("  "," ")
print(mt)
# Problem 5
old_letter = "Dear Harry, This python course is nice! Thanks!"
print(old_letter)
new_letter = "Dear Harry, \n\tThis python course is nice! \nThanks!"
print(new_letter)