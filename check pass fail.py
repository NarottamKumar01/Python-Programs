sub1=int(input("enter first marks:",))
sub2=int(input("enter second marks:",))
sub3=int(input("enter third marks:",))
sub4=int(input("enter fourth marks:",))
sub5=int(input("enter fifth marks:",))
avg=(sub1+sub2+sub3+sub4+sub5)//5
if avg>=40 and avg<50 :
    print("pass with third division and the percent is:",avg)
elif avg>=50 and avg<60:
    print("pass with second divison and the percent is:",avg)
elif avg>=60 :
    print("pass with first division and the percent is:",avg)
else:
    print("fail and the percent is",avg)
 
