x = 40              #global variable
def localfunction():
    result = x*2    #result = local variable
    print(result)

print(result)

localfunction()