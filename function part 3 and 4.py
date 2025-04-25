#when function return nothing  in actual it returns none
def add():
    print("hello")
x=add()
print(x)
print(type(x))
#default arguements
def sum(a=0,b=0,c=0): #here a, b, c is like default value arguement
    s=a+b+c
    print("sum is",s)
sum()
sum(10)
sum(10,20)
sum(10,20,30)
#we have to pass the arguement as per formal arguement we have paas while defining the function
#or we can defined or use default value
#after default value we can't take non default value
#keyword arguement:- means position se koi farq nhi padta
def f1(a,b):
    print("a=",a,"b=",b)
f1(10,20) #here like position of a and b are fixed so its positional arguement
f1(b=20,a=10) #here keyword arguement used which was used in formal arguement 
#positinal arguement follow keyword arguement..means 1st postional arguement then keyword arguement
#like
f1(10,b=20)# here 10 act as positional arguement and b=20 act as keyword arguement
