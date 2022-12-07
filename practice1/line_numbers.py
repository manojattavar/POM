file = "C:\\Users\\029693744\\PycharmProjects\\InterviewPractice\\practice\\largeFile"

def fileCount(file):
    with open(file) as f:
        for i in enumerate(f):
            pass
        return i

count = fileCount(file)
print(count)
