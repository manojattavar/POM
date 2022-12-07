
def fib():
    num = int(input("Enter a number: "))

    n1 = 0
    n2 = 1
    i = 0

    if (num <= 0 ):
        print("Enter a positive number")

    elif (num == 1):
        print("Fibonacci series is 0 and 1")

    else:
        while (i < num):
            n = n1 + n2
            print(n, end=",")
            n1 = n2
            n2 = n
            i += 1

fib()