num = int(input("num: "))
fact=1
for i in range(num,0,-1):
    fact=fact*i
    #print(fact,"*",i)
print(fact)