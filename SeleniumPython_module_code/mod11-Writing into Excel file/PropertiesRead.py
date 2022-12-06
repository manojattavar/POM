'''
Created on 05-Mar-2020
@author: Jaspreet
'''
from configparser import ConfigParser
from os import path
c = ConfigParser()
# c.read("D:\\eclipse\\workspace\\SeleniumPython\\module09\\properties.properties")
c.read(path.abspath(path.pardir)+"\\properties.properties")

a=c.sections()
print(a)

print(c['Section_name']['name1'], " : ",c['Section_age']['age1'])
print(c['Section_name']['name2'], " : ",c['Section_age']['age2'])

print("")
print(dict(c.items('Section_name')))
print(dict(c.items('Section_age')))