'''#how to modify file content
f=open("file1.txt","r+")
x="Indore\n"
l=0
s=f.readline()
while True:
    if s=='':
        break
    l+=len(s)
    if s==x:
        f.seek(l-len(s)+1,0)
        f.write("INDORE\n")
        break
    s=f.readline()
    
f.close()'''
#how to write in a object file:
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
students_list=[Student('Amit',19),Student('Rohan',19),Student('Rahul',19)]
def saveStudents():
    import pickle
    f1=open('file2.obj','wb')
    for s in students_list:
        pickle.dump(s,f1)
    f1.close()
def ViewAllStudents():
    import pickle
    f2=open('file2.obj','rb')
    s_list=[]
    while True:
        try:
            s_list+=[pickle.load(f2)]
        except EOFError:
            break

    return s_list
saveStudents()
l=ViewAllStudents()
for e in l:
    print(e.name,'....',e.age)
            
    
