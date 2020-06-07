"""
Difference between __str__ and __repr__ functions

    __str__ must return string object whereas __repr__ can return any python expression.
    If __str__ implementation is missing then __repr__ function is used as fallback. There is no fallback if __repr__ function implementation is missing.
    If __repr__ function is returning String representation of the object, we can skip implementation of __str__ function.


Earlier we mentioned that if we don’t implement __str__ function then the __repr__ function
is called. Just comment the __str__ function implementation
from Person class and print(p) will print {name:Pankaj, age:34}.
Summary

Both __str__ and __repr__ functions are very similar. We can get the object representation
in String format as well as other specific formats such as tuple and dict to get information
 about the object.
"""


class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return {'name':self.name, 'age':self.age}

    # __repr__ also implement as string
    def __repr__(self):
        return '{name:' + self.name + ', age:' + str(self.age) + '}'

    # def __str__(self):
    #     return 'Person(name='+self.name+', age='+str(self.age)+ ')'


p = Person('Rahul', 34)
print(p)
print(p.__str__())
print(type(p.__str__()))
s = str(p)
print(s)
print(p.__repr__())
print(type(p.__repr__()))
print(repr(p))

