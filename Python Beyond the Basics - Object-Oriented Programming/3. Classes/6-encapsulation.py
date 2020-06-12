"""
In an object oriented python program, you can restrict access to methods and variables.
This can prevent the data from being modified by accident and is known as encapsulation.

Or
Encapsulation the first pillar of OOPs
Encapsulation refers to the safe storage of data (as attributes ) instance
Data should be accessed only through instance methods
Data should be validated as correct(depending on the requirement set in in the class method)
Data should be safe from changes by external processes

This provide the gateway to access the data

========================================
What is mean by breaking the encapsulation
-setting the value without setter method it is breaking the encapsulation that
it big no no

or
-All though normally set in a setter method,instance attribute value can be
set anywhere
-Encapsulation in python is a voluntary restriction.
-Python does not implement data hiding as other language.


===========================================
THe way to inforce the encapsulation and take control of attribute setting
Even that it is done derectly in object so that we can again ensure the intigrity of  an data
going in and reject any that not working.

"""


class MyInteger(object):
    def set_value(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.value = val

    def get_value(self):
        return self.value

    def increment(self):
        self.value = self.value + 1


i = MyInteger()
i.set_value(10)
print(i.get_value())
i.value = 'hi'
print(i.value)
# print(i.increment())


