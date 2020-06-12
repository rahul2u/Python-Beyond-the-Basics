"""
Attributes/variables in the class are accessible through instance
Instance attributes are also accessible by instance
When we use hte syntex object.attributes we are asking python to look the attributes
    first in the instance
    then in the class
Method calls through the instance follow the lookup


"""


class MyClass(object):
    classy = "This is class value "


dd = MyClass()
print(dd.classy)
dd.classy = "This is instance"
print(dd.classy)
del dd.classy
print(dd.classy)

dd.name = "Rahul Singh"
print(dd.name)