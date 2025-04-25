#opps
#syntax of class
class Test:
    i=10
    def f1():
        print("Hello")
print(Test.i)
Test.f1()
t1=Test()
#print(t1)
#class store both as attribute
#variable
#function 
#defining init method like __init__(): init function always take atleast 1 arguements
class Test:
    i=10
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("init")
    def f1():
        print("Hello")
t1=Test(3,4)
print(Test.i)
Test.f1()
class Test:
    def __init__(self,x,y):
       self.a=x
       self.b=y

       
t1=Test(3,4)
t2=Test(6,8)
t3=Test(10,12)
print(t1.a,t1.b)
print(t2.a,t2.b)
print(t3.a,t3.b)
