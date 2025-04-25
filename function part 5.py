#variable length arguements
def avg(*n):
    s=0
    for x in n:
        s=s+x
    if len(n)>0:
        return s/len(n)
    return "no element"
    #print(n,type(n)) here n is of tuple type 
y=avg(10,20,30,40)
print(y,"is avg")
def avg(a,b):
    c=(a+b)/2
    return c
x=avg(10,20)
print(x)
print("Avg is ",x)
# but to calculate more than two number of avg we have to used variable length of arguement like *n in place of formal argueme
def f2(playername,*points):
    print(playername,end=' ')
    s=0
    for x in points:
        s=s+x
    print("Total points=",s)
f2("ajay",10,11,12,13)
#2nd method with use of keyword arguement..
def f2(*points,playername):
    print(playername,end=' ')
    s=0
    for x in points:
        s=s+x
    print("Total points=",s)
f2(10,11,12,13,playername="ajay")
#variable length keyword arguement ** use karne pr dict bnta hai
def f1(**k):
    print("person information")
    for key,value in k.items():
        print(key,"-",value)
f1(name="sameer",age=22)
f1(name="sameer",age=23,marks=87)
f1(name="sameer",empid=125,salary=25000.0)
