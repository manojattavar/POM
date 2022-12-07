
def prime():
    num = int(input("Enter a num: "))
    flag = False

    if (num < 2):
        print(str(num) + " is a prime number")
    else:
        for i in range(2, num):
            if (num % i == 0):
                flag = True
        if (flag):
            print(str(num) + " is not a prime number ")
        else:
            print(str(num) + " is a prime number ")

prime()
