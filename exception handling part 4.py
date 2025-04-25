#exception handling of nested try block
try:
    print("line1")
    print("line2")
    print("line3")
    try:
        print("line4")
        print("line5")
        3/0
        print("line3")
    except ZeroDivisionError:
        print("except1")
    finally:
        print("finally")
    print("line5")
except TypeError:
    print("except2")
finally:
    print("finally2")
 
