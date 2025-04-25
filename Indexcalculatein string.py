s1="mysirg education services"
print(s1.index("e"))
print(s1.index("a"))
print(s1.index("t"))
print(s1.index("v"))
print(s1.count("e"))
#negative indexing
print(s1[-2])
#slicing opertaor
print(s1[7:16])
print(s1[2:-2])
print(s1[5:23])
#for reverse using slicing operator
print(s1[-5:8:-1])
print(s1[24::-1])
print(s1[len(s1)::-1])
print(s1[2:23:2])
print(s1[-2:1:-1])
#convert the string into upper case or lower case
print(s1.lower())
print(s1.upper())
#to check the particular pattern in string
print(s1.startswith("my"))
print(s1.endswith("services"))
print(s1.endswith("my"))
#to split the string
print(s1.split(" "))
