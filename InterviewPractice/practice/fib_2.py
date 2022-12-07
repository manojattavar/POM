

def fib():
    num = int(input("Please enter a number = "))

    n1 = 0
    n2 = 1

    x = 0

    if (num <= 0):
        print("Please enter a positive number...")
    elif (num == 1):
        print("Fibonacci series upto 1")
        print(n1)
    else:
       print("Fibonacci sequence...")
       while(x<num):
           print(n1)
           n = n1 + n2
           n1 = n2
           n2 = n
           x += 1
fib()