month = int(input("enter month number"))

if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    print("month have 31 days")
elif month == 4 or 6 or 9 or 11:
    print("month have 30 days")
elif month == 2:
    print("month have 28 days")
