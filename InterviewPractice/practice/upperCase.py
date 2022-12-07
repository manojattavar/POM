file = "C:\\Users\\029693744\\PycharmProjects\\InterviewPractice\\practice\\largeFile"

with open(file) as countletter:
    count = 0
    text = countletter.read()
    for character in text:
        if character.isupper():
            count += 1
    print(count)
