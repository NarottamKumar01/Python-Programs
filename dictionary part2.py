#writting a program to take data from user in dictionary and perform it and we have start word from these letter
words={}
l=['a','b','c','d']
for x in l:
    print("Enter word for letter",x)
    words[x]=input()
print(words)
# how to remove data or delete data from dictionary in case of delete we have to write data complete not just key
#like if we want to delete pairs
print(words)
del(words['c'])
print(words)
#copy function
words.copy
print(words)
#clear function delete all pair items in dictionary
words.clear()
print(words)

d1={1:"A",2:"B"}
print(d1)
d=d1.copy() #shallow copy means copy as it is
print(d)
print(id(d1))
print(id(d))
print(d is d1)#true if both same and false if both different
#fromkeys function
l=[1,3,4,5]
print(d.fromkeys(l,"abc"))
print(d)
d2=d.fromkeys(l,"abc")
print(d2)
#get function is similar like using key inplace of index get function not give key error but using key give error if going out of range
#get function out of range give output as None
print(d.get(2))
print(d[2])
x=d.get(3)
print(x)
print(type(x))
#pop function we give key and value is come as output means return value not the pair and it take key in arguement
d2={1:"A",2:"B",3:"C"}
print(d2)
y=d2.pop(2)
print(y)
print(d2)
#popitem means it will pop any one item and it not take any arguement and return as tuple that item
d2={1:"A",2:"B",3:"C"}
z=d2.popitem()
print(z)
#we can do indexing then after return as tuple
print(z[0])
print(d2)
#d={1:"abc"} : call dict item where 1 is dict key and "abc" is dict value
