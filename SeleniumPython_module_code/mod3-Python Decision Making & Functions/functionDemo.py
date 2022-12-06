def sum1():
    num1 = 50
    num2 = 89
    result = num1+num2
    print("Output of addition of "+str(num1)+ " and "+str(num2)+ " : "+str(result))

def sum2(num1, num2):
    result = num1 + num2
    print("Output of addition of " + str(num1) + " and " + str(num2) + " : " + str(result))

def sum3():
    num1 = input("Enter num 1 : ")
    num2 = input("Enter num 2 : ")
    result = int(num1) + int(num2)
    print("Output of addition of " + str(num1) + " and " + str(num2) + " : " + str(result))

def sum4():
    num1 = input("Enter num 1 : ")
    num2 = input("Enter num 2 : ")
    result = int(num1) + int(num2)
    return result

# sum2(96,48)
# sum3()
# print("Output is  : "+str(sum4()))