import math
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
D=b**2-4*a*c
if a==0:
    print("not a quadratic equation")
elif D==0:
    print("roots are real and equal")
elif D<0:
    print("roots are imaginary")
elif D>0:
    print("roots are real and unequal")


