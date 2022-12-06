'''
Created on 16-Mar-2020
@author: jaspreet
'''
def numbers(no):
    result = []
    for i in no:
        result.append(i*i*i)
    return result

num = numbers([1,2,3,4,5])
print(num)

print("- - - - - - - - - - - - - - - - - - - - - ")

def number(no):
    for i in no:
        yield i*i*i
        
nums = number([1,2,3,4,5])
for i in nums:
    print(i)