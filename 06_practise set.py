# Problem 1(Find greatest)
'''num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))
if (num1>num4):
    f1=num1
else:
    f1=num4
if (num2>num3):
    f2=num2
else:
    f2=num3
if (f1>f2):
    print(str(f1)+"is greatest")
else:
    print(str(f2)+"is greatest")'''
# Problem 2(Marks problem)
'''sub1 = int(input("Enter first subject marks:\n"))
sub2 = int(input("Enter second subject marks:\n"))
sub3 = int(input("Enter third subject marks:\n"))
if (sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif (((sub1+sub2+sub3)/34333)<40):
    print("Your are fail as your percentage is less than 40")
else:
    print("Congratulations!you have passed the test")'''
# Problem 3(Spam detector)
'''text = input("Enter text\n")
if ("make a lot of money"in text):
    spam=True
elif ("subscribe now"in text):
    spam=True
elif ("click this"in text):
    spam=True
else:
    spam=False
if(spam):
    print("This text is spam")
else:
    print("This text is not spam")'''
# Problem 4(Less than 10 character)
'''a = input("Enter character\n")
if (len(a)<10):
    print("The no. of characters are less than 10")
else:
    print("The no. of characters are more than 10")'''
# Problem 5 (Check whether the entered name is present in list or not)
'''names = ["Rishu","Aditya","Aakash","Nirbhay","Himanshu"]
name = input("Enter your name\n")
if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")'''
# problem 6 (Marks grading)
'''marks = int(input("Enter your marks:\n"))
if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
else:
    grade = "F"
print("Your grade is "+grade)'''
# Problem 7(Talking about Rishu or not)
a = "RISHU"
b = "Rishu"
c = "rishu"
d = "rISHU"
sen = input("Enter any sentence:\n")
if a in sen:
    print("It is talking about Rishu")
elif b in sen:
    print("It is talking about Rishu")
elif c in sen:
    print("It is talking about Rishu")
elif d in sen:
    print("It is talking about Rishu")
else:
    print("Not talking about Rishu")