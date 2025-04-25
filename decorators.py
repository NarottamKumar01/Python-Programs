#function decorators is a type of function to decorate function
def decor_result(result_function):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("congrats! you have got distinction")
        else:
            result_function(marks)
    return distinction
@decor_result             #it show that decorators have to be called:-
def result(marks):
    for m in marks:
        if m>=33:
            pass
        else:
            print("fail")
            break
    else:
        print("PASS")
result([50,40,50,60,90,80])

