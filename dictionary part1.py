#dictionary contain key value pair and in dictionary use map function:
#each element of a dictionary is a pair of key value
#key can not be repeat , key must be unique. two key can't be same
# repeattation in case of value possible means for 1 key two value possible;
#key and value  can be of any type
#key and value can be of hetrogeneous type data
#indexing is not possible in dictionary because specific order not fixed for key value order
#slicing operator do not work
#dictionary is mutuable.means we can add edit delete
#we can do grow and shrink memory in dictionary


#how to create a dictionary
d={}
print(type(d))
# we can use constructor dict
d=dict()
print(d)

# how to keep value inside dictionary but we have to keep value in pairs like key value 
d={100:'Rahul',200:'ajay'}
print(d)
d1={"a":"apple","b":"banana"}
print(d1)
#while using dict constructor we don't use colon(:) in place of that we use = here we don't write key in quotes and keys can't be numbers 
d2=dict(a="apple",b="ball",k="allow")
print(d2)
#how to access dictionary but in place of indexing we write key there but in string type
d2=dict(a="apple",b="ball",w="allow")
print(d2['a'])
#adding element in dictionary after making dictionary
#assigning the value in dictionary also
d={1:"A",2:"B",3:"C"}
print(dict(d))
d[5]="E"
print(d)
#we can replace the key value if key value is same then new one is came and call that how to edit in dictionary
d[1]="a"
print(d)
#to print each element in new line
for k in d:
    print("Key=",k," Value=",d[k])

d1={1:"a",2:"b",3:"c",4:"d"}
print(dict(d1))
d1[5]="e"
print(d1)
print(d1[1])
print(d1[2])


