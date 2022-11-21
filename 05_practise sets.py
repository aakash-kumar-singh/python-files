#Problem 1

myDict = {
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Things",
}
print("Options are",myDict.keys())
a = input("Enter the Hindi word\n")
# print("The meaning of your word is:", myDict[a])
# Below line will not throw an error if the key is not present in the dictionary.
print("The meaning of your word is:", myDict.get(a)) # This will return none if the word is not present in the dictionary.

#Problem 2
num1 = int(input("Enter num1\n"))
num2 = int(input("Enter num2\n"))
num3 = int(input("Enter num3\n"))
num4 = int(input("Enter num4\n"))
num5 = int(input("Enter num5\n"))
num6 = int(input("Enter num6\n"))
num7 = int(input("Enter num7\n"))
num8 = int(input("Enter num8\n"))

s = {num1,num2,num3,num4,num5,num6,num7,num8}
print(s)

# Problem 3
s = {18,"18",18.1}#All have different meaning for set
print(s)

# Problem4
A = set()
print(len(A))
A.add(20)
A.add(20.0)
A.add("20")
print(A)
print(len(A))

# Problem 5 
m = {}
print(type(m))