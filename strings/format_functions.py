"""
Sample code of string concatenation
"""

name = 'Mark'
age = 31
message = 'Hello ' + name + ' (' + str(age) + ')'
message1 = 'Hello Again {} ({})'.format(name, age)
print(message)
print(message1)

