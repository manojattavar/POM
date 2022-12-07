
count = 0
with open("C:\\Users\\029693744\\PycharmProjects\\pythonInterview\\text") as file:
    letter = file.read()
    for i in letter:
        if (i.isupper()):
            count += 1
    print(count)