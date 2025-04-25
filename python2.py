dict={}
print(dict)
print(type(dict))
dict['one']='Ram'
dict['two']='Sham'
print(dict)
inventory={'apple':430,'banana':3000,'orange':560,'pears':32}
print(inventory)
del inventory['pears']
print(inventory)
inventory['Avacado']=0
print(inventory)
print(len(inventory))
print(inventory.keys())
print(inventory.values())
opposite = {'up':'down', 'right':'wrong','true':'false'}
alias = opposite
copy = opposite.copy()
opposite['right']='left'
print(alias)
print(opposite)
print(copy)
print(opposite)
matrix={(0,3):1,(2,4):2(4,3)}
print(matrix[0,3])
print(matrix.get(1,1),0)
print(matrix.get(1,2),0)
a={1:"A",2:"B",3:"C"}
for i,j in a.items():
    print(i,j,end="")

