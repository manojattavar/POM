file = "C:\\Users\\029693744\\PycharmProjects\\InterviewPractice\\practice\\largeFile"

with open(file) as text:
    count = 0

    char = text.read()

    for i in char:
        if i.isupper():
            count += 1

    print(count)