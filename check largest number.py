x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))
if (x>=y) and (x>=z):
    greatest = x
if (y>=x) and (y>=z):
    greatest = y
if (z>=y) and (z>=x):
    greatest = z
print("the greatest number is",greatest)
