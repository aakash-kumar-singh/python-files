# Problem 1(print table of given number)
'''num = int(input("Enter number: "))
for i in range(1,11):
    print(str(num)+"X"+str(i)+"="+str(i*num))'''

# Problem 2 (print hello before names)
''''l1 = ["Harry","Sohan","Sachin","Rahul"]
for name in l1:
    print("Hello",name)'''
# Problem 2 (print hello before names starting with S)
'''l2 = ["Harry","Sohan","Sachin","Rahul"]
for name in l2:
    if name.startswith("S"):
        print("Hello",name)'''
# Problem 3(Attempt problem 1 using while loop)
'''num = int(input("Enter number: "))
i = 1
while i<=10:
    print(str(num)+"X"+str(i)+"="+str(num*i))
    i = i+1'''
# Problem 4 (Check whether the number is prime or not)
'''num = int(input("Enter number: "))
prime = True
for i in range(2,num):
    if (num%i==0):
        prime = False
        break
if prime:
    print("This number is prime")
else:
    print("This number is not prime")'''
# Problem 5 (sum of first n natural numbers)
'''n = int(input("Enter number of terms: "))
i = 1
sum = 0
while i<=n:
    sum = sum+i
    i = i+1
print(sum)'''
# Another method for above question
'''n = int(input("Enter number of terms: "))
sum = 0
for i in range(0,n+1):
    sum+=i
    i = i+1
print(sum)'''

# Problem 6 (Find the factorial of a given number)
num = int(input("Enter number: "))
fact = 1
for i in range(1,num+1):
    fact=fact*i
    i = i+1
print(f"The factorial of {num} is {fact}")

