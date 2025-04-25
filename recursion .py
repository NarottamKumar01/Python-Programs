#recusion:- means function calling itself
def sum(n):
    if (n==1):#base case 
        return 1
    else:
        return n+sum(n-1)#recursive case
sum(10)
#advantage of recursion that code easily formulate
#3step for recursion 1.define function 2.recursive case 3.base case
