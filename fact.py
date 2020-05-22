num=int(input("number:"))

fact=1

if num <0:
    print("must be positive")
elif num == 0:
    print("fact = 1")
else:
    for i in range(1,num+1):
        fact=fact*i

print(fact)