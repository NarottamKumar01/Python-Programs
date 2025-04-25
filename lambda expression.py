#lambda expression or anonymus function(means function without name) lambda is keyword
s=lambda a,b:a+b
r=s(10,20)
print("sum is",r)
#syntax lambda arguements:single expression
# create a lambda expression and find the greater number between two number
print("enter two numbers")
a=int(input("enter first number"))
b=int(input("enter second number"))
s=lambda a,b:a if a>b else b
y=s(a,b)
print("greatest number is",y)
#recursion in lambda expression
def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
s=fact(5)
print("factorial is",s)
#now through lambda expreesion
s=lambda a:1 if a==0 else a*s(a-1)
r=s(7)
print(r)
