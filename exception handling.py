#exception handling 1.syntax error 2.Runtime erroror exception error
'''x=int(input("enter first number"))
y=int(input("enter second number"))
print("sum is",x+y)'''
#TypeError
#ZeroDivisionError
#AutomaticallY raise Exception like above two
#agar exception aaya to uske aage ki line nhi chalegi
#pre defined exception like already builtin
#user defined exception like we have defined
#total 4 keyword used 1.try 2.except 3.finally 4.raise
#try block me possible risky code use colon(:)
#then statement then except block with exception class name use colon(:)
x=int(input("enter first number"))
y=int(input("enter second number"))
try:   
    z=x+y
    print("sum is",z)
except ZeroDivisionError:
    print("invalid attempt of addition")
finally:
    print("In finally")
print("hello world")
#rule of try and except
'''1.try block me wo code likhna h jisme error aane ki sambhavna h
2.no except block without try block
3.no exception raise in try then except block skipped
4.multiple except block for single try possible
5.finally runs always
6.try--except--finally
7.more than one finally block can't possible
8.inside try block either we have to either mention except or finally block atleast anyone of these
9.multiple try blocks even possible
10.else can be used in try block
11.else used when no exception raised
'''
 
