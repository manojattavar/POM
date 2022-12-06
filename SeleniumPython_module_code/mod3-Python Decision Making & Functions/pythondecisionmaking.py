#if statement
a = 3
if(a<10):  #condition is satisfied = boolean True
    # condition is not satisfied = boolean False
    print("a is less than 10")

#if-else statement
a = 50
if(a<10):
    print("a is less than 10")
else:
    print("a is greater than 10")

#if-elif-else statement
a = 50
if(a==10):
    print(a)
elif(a==50):
    print(a)
else:
    print("a is undefined")

#nested if statement
a = 0
if(a!=0):
    if(a<40):
        print("a is less than 40")
    else:
        print("a is greater than 40")
else:
    print("a is zero")

