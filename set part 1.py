s={10,20,30}
print(type(s))
#how to create a set
s={}
print(type(s))
s=set()
print(type(s))
'''s=set(10)
print(s)'''
'''s=set(1,2,3)
print(s)'''
s=set([1,2,3,4])
print(s)
print(type(s))
s=set("my sirg.com")
print(s)
list=[1,2,3,1,3,1]
s=set(list)
print(s)
s=set((10,20))
print(s)
s=set("ababababab")
print(s)
s={1,2,3,4}
s.add(5)    
print(s)
#set can take hetrogeneous data
#duplicate element will not put any effect on set
l=[1,3,4,6,7]
s={1,2,3,4}
s.update(l)
print(s)
#update function take union 
#discard method - if item not found in sequence then it donot show any error.. 
s.discard(4)
print(s)
#remove method :- if item not found in sequence it show error..
s.remove(6)
print(s)
#list can not be as an element inside set..
#s={1,2,(3,4),[5,6]}
s={1,2,(3,4)}
s.discard(2)
print(s)
# to find common between two set like intersection
s1={1,2,4,5}
s2={2,3,4,6}
print(s1.intersection(s2))
# clear function remove all element
s2.clear()
print(s2)
#like intersection we can use union
s1={1,2,4,5}
s2={2,3,4,6}
print(s1.union(s2))
s1={1,2,4,5}
s2={2,4}
print(s2.issubset(s1))
s1={1,2,4,5}
s2={2,4}
print(s1.issuperset(s2))
s1={1,2,4,5}
print(s1.pop())
print(s1)
s1={1,2,4,5}
s=s1.copy()
print(s)
print(id(s1))

