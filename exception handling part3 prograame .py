class InsufficientBalance(ZeroDivisionError):
    def __init__(self,arg):
        self.msg=arg
balance=5000
w=int(input("enter amount to withdraw"))
try:
    if w>balance:
        raise InsufficientBalance("Insufficient Balance in the account")
    balance=balance-w
except InsufficientBalance as i:
    print("exception",i.msg)
else:
    print("withdraw amount",w,"successfully")
finally:
    print("Current balance is",balance)
