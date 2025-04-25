#type of variable
#1.instance variable :object specific information
#2.static variable
#3.local variable
#4.Global variable
#creating class then using 1st type and how to create instance variable using 3 method
'''class Account():
    def __init__(self,a,b):
        self.accountnumber=a
        self.balance=b
    def f1(self,a,b):
        self.accountnumber=a
        self.balance=b
acc1=Account()
acc1.f1(101,4000)
acc1.accountnumber=102
acc1.balance=10000
print(acc1.__dict__)
accountnumber1=Account(100,5000)
accountnumber2=Account(200,6000)
accountnumber3=Account(500,7000)
print(accountnumber1.__dict__)
print(accountnumber2.__dict__)
print(accountnumber3.__dict__)
'''
#static variable
