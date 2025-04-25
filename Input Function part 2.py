#reading multiple value
x,y=input("enter first number"),input("enter second number")
print(x)
print(y)
#or second method
x,y=input("enter two numbers").split(',')
print(x,y)
#in this we get output in form of list of string and and is seprated by space if we donot pass arguement
#but we can pass like comma(,) etc.
x=input("enter few words").split()
print(x)
#output we get in form of list of string
x=input("enter date").split('/')
print(x)
#in case of multiple variable.
a,b,c=input("enter date").split('/')
print(a,b,c)
#want to print without string then
a,b,c=[int(x) for x in input("enter date").split('/')]
print(a,b,c)
