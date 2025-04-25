'''f=open('file1.txt','w')
text=input("enter some text")
f.write(text)
f.close()
f=open('file1.txt','w')
l=["Bhopal\n","delhi\n","chennai\n","mumbai"]
f.writelines(l)
f.close()
f=open('file1.txt','r')
print(f.read())
f.close()
f=open('file1.txt','r')
print(f.read(5))
f.close()
f=open('file1.txt','r')
print(f.readline())
f.close()
f=open('file1.txt','r')
for line in f:
    print(line)
f.close()
f=open('file1.txt','r')
s=f.readline()
print(s)
f.close()'''
f=open("file1.txt","r")
s1=f.readlines() #return list of string
x=input("enter your city name")
x+="\n"
for e in s1:
    if e==x:
        print("city matched",e)
f.close()
