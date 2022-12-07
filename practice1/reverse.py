file = "C:\\Users\\029693744\\PycharmProjects\\InterviewPractice\\practice\\largeFile"

import random
def read_random(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

read_random(file)