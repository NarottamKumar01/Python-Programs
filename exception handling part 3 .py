#raise exception class
x=int(input("enter a number"))
y=int(input("enter a number"))
try:
    if y==0:
        raise ZeroDivisionError("Denominator cannot be zero") 
    z=x/y
    print("division is",z)
except ZeroDivisionError:
    print("you cannot divide by zero")

