#multiple value with different different type
a,b,c=[eval(x) for x in input("enter date").split(',')]
print(a,b,c)
#geeting error because list type value not work in eval function
print(type(a))
print(type(b))
print(type(c))
#want to take value from user but input is sequence like list tuple dictionary set etc
l=[eval(x) for x in input("enter three values").split(',')]
print(l)
#in case of tuple we use tuple as constructor
l=tuple([eval(x) for x in input("enter three values").split(',')])
print(l)
#for set we use set as constructor
l=set([eval(x) for x in input("enter three values").split(',')])
print(l)
#for dictionary
l=dict( input().split('-') for _ in range(3))
print(l)
d={x:input() for x in range(1,5)}
print(d)
d1={input("key"):input("value") for x in range(3)}
print(d1)
