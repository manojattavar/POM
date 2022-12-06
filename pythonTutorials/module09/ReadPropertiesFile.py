from configparser import ConfigParser

c = ConfigParser()
c.read("C:/Users/029693744/PycharmProjects/pythonTutorials/module09/properties.properties")

a = c.sections()
print(a)

print(c['Section_name']['name1'])