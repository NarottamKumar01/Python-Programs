a=int(input("enetr smaller number"))
b=int(input("enetr greater number"))
s=range(a,b)
for x in s:
    for num in range(2,x):
        if x%num==0:
            break
    else:
        print(x,"prime in range")
        break
