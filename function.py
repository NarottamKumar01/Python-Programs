#function is a block of code..increase the resusability
#we use function to reduce the repeatation of work
#function has some name
#check indentation
#how to creatye function in python?
#def function_name():
def add():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a+b
    print("sum is",c)
#how to used or call function?
print("Hello this is first line")
add()
print("this is a line after first call to the function add")
add()
#two types of function
#(1) pre defined function: already defined means built in
#(2) user defined function: we have defined that
#4ways to define function
#if paranthesis of function is empty then it is take nothing nature and if have something then it is take something in nature..
#variable inside the function is local variable.in above example a b s are local variable
#return nothing means no using of return keyword
#type 1
def add():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a+b
    print("sum is",c)
add()
#type2
def add(a,b):#here a and b are formal arguement
    c=a+b
    print("sum is",c)
add(10,20)# call ke time wala actual arguements hai
#type 3
def add():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a+b
    return c                     #means in place of print we use return keyword 
x=add()
print("x=",x)
#type4
def add(a,b):
    c=a+b
    return c
w=add(10,20)
print("sum is",w)

