

def fib():
    num = int(input("Enter a number = "))

    n1 = 0
    n2 = 1

    x = 0

    if (num < 1):
        print("Pleae enter a positive number ")

    elif (num == 1):
        print("fibanacci series for ", num)
        print(n1)
        
    else:
        while (x < num):
            print(n1, end=', ')
            n = n1 + n2
            n1 = n2
            n2 = n
            x += 1

fib()