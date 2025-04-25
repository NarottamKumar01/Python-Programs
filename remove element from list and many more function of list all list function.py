#how to remove element in list
mylist=[10,20,30,40,50]
mylist.remove(30)
print(mylist)

d=[1,2,3]
d*=3
print(d)
d.remove(2)
print(d)
d.sort()
print(d)
d.clear()
print(d)

s=[1,2,3,4,5,6]
s.reverse()
print(s)

z=[1,2,3,4,5,6,7,8,9]
z.pop()
print(z.pop())
print(z)
z.remove(5)
print(z)
z.pop(4)
print(z.pop(4))
print(z)
A=[10,20,30,40,50,60]
A.index(30)
print(A.index(30))
c=[1,2,1,3,2,1,3,2,1,3,2,3]
c.index(1)
print(c.index(1))
c.index(3,1)
print(c.index(3,1))
c.index(1,2,12)
print(c.index(1,2,12))
c.index(1,8,12)
print(c.index(1,8,12))

#count number how many times came
B=[1,2,3,1,3,2,1,3,4,5,1,1,2]
B.count(1)
print(B.count(1))
