t=()
print(type(t))
t2=(10)
print(type(t2))
t3=(10,)
print(type(t3))
t1=(1,2,3,4,5)
print(type(t))
#convert list to tuple
list=[1,2,3,4,5]
t=tuple(list)
print(t)
print(type(t))
print(type(list))

mytuple=(10,20,30,"india")
print(type(mytuple))
mytuple=(10,20,30,"india")
print(mytuple[1])

t=(10,20,30,40)
i=0
while i < len(t):
    print(t[i])
    i+=1


tuple=(1,2,3,4,5,6)
for x in tuple:
    print(x)

#print square of each element of tuple in new line 
t=(10,20,30,40)
for x in t:
    print(x*x)

tuple=(10,20,30,40,50)
print(tuple[0:6:1])
# how to add element in tuple means two tuple merge to form a new tuple
t=(10,20,30,40,50)
t=t+(1,2,3,4,5,6)
print(t)
print(t[0::2])
print(t[2:5:1])
#packing and unpacking in tuple
#packing combining variable to form a tuple
a=1
b=2
c=3
t=(a,b,c)
print(t)
#unpacking means breaking a tuple into variables
tuple=(1,2,3,4,5)
a,b,c,d,e=tuple
print(a,b,c,d,e)
print(type(a))
#concatenation
a=(1,2,3)
b=(10,20,30)
print(a+b)
#repeatation operator
t=(1,2,3,4)
print(t*3)
#comparison in tuple
a=(1,2,3)
b=(1,2,3,4)
print(a==b)
print(b>a)
#how to take data input from user in tuple
x=input("enter a tuple")
print(x)
print(type(x))
x=eval(input("enter a tuple"))
print(x)
print(eval("5+2"))
#write a program in which you have to take input from user and caclculate there sum
x=eval(input("Enter a Tuple"))
s=0
for e in x:
    s=s+e
print("Sum is ",s)
#function in Tuple
x=(1,2,3,4,1,2,1,1)
print(len(x))
print(x.count(1))
print(x.index(3))





