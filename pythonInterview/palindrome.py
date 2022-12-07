
def palindrome(x):
    for i in range(0, int(len(x)/2)):
        if (x[i] != x[len(x) -i -1]):
            return False
        return True

x = "malayalam"
if (palindrome(x)):
    print(x, " is a palindrome ")
else:
    print(x, " is not a palindrome ")