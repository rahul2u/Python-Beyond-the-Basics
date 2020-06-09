"""
Instance attributes or object attributes (State)
 attributes
     class attributes - define in class
     instance attributes - genrally state of current object ex-car - spped, millage
============================
Self is instance upon which the method was called.
how objects themselves can have their own attributes.
unit of data we've been talking about the attributes that can be associated with an instance or an object.
This is the data that we were talking about when we said that an object is a unit of data.
Again we call the attributes of an instance the State of the instance.

=================================================
-We have seen that instance can access variables defined in the class
-An instance can also get and set values itself
-Because the values is change according to what happens to object, we call these values state.
-Instance data  takes the form of instance attributes values set and acessed through object.attributes sysntx



"""
import random


class MyClass(object):
    def my_function(self):
        self.val = random.randint(1, 10)


myobj = MyClass()
myobj.my_function()
print(myobj.val)
