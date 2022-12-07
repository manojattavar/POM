file = "C:\\Users\\029693744\\PycharmProjects\\InterviewPractice\\practice\\largeFile"

with open(file) as countLetters:
    count = 0
    text = countLetters.read()
    for i in text:
        if (i.isupper()):
            count += 1
    print(count)