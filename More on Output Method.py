Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#print variable value
x=10
print(x)
10
x=10
y=20
print(x,y)
10 20
#want to remove gap between 10 and 20 and seprated by comma
print(x,",",y)
10 , 20
#still spaces then
print(x,y,sep=',')
10,20
10,20
(10, 20)
print(x,y,sep=":")
10:20
print("AB"+"CD")
ABCD
print("AB","CD")
AB CD
print("AB","CD",sep="/n")
AB/nCD
print("AB","CD",sep="\n")
AB
CD
x=10
y=20
z=30
print(x,y,z sep=",",end=".")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(x,y,z,end=".", sep=":")
10:20:30.
x=10
print("value of x is %d" %x)
value of x is 10
a=2
b=3
>>> c=4
>>> d=5
>>> e=a+b+c+d
>>> print("sum of %d and %d and %d and %d is %d" %(a,b,,c,d,e))
SyntaxError: invalid syntax
>>> a=2
... b=3
... c=4
... d=5
... e=a+b+c+d
... print("sum of %d and %d and %d and %d is %d" %(a,b,c,d,e))
SyntaxError: multiple statements found while compiling a single statement
>>> a=2
... b=3
... c=a+b
... print("sum of %d and %d is %d" %(a,b,c))
SyntaxError: multiple statements found while compiling a single statement
>>> a=2
... b=3
... c=a+b
... print("Sum of %d and %d is %d" %(a,b,c))
SyntaxError: multiple statements found while compiling a single statement
>>> a=3
>>> b=4
>>> c=a+b
>>> print("Sum of %d and %d is %d" %(a,b,c))
Sum of 3 and 4 is 7
>>> x=10
>>> y=3.5
>>> print("x=%d y=%f" %(x,y))
x=10 y=3.500000
>>> x=10
>>> print("x=%g" %x)
x=10
>>> x=10.1542
>>> print("x=%g" %x)
x=10.1542
>>> x=5
>>> y=3.5
>>> z="narottam"
>>> print("Hello, ",z,"x=",x," y=",y)
Hello,  narottam x= 5  y= 3.5
>>> print("Hello, {2} x= {0} y= {1}".format(x,y,z))
Hello, narottam x= 5 y= 3.5
>>> print("Hello,{2} x= {0} y= {1}".format(x,y,z))
Hello,narottam x= 5 y= 3.5
