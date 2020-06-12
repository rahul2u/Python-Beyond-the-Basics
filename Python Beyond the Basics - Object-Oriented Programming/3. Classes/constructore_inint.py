"""
__init__ - Private method or magic method it's intended to be used internally not called by the
user of the class and it's called magic because it's usually called automatically when a particular event happens
__init__ private method that allow to initialized the attributes of the instance is constructed
-As you seen previous video the attributes are set the by setter method
- If you want to some attributes at the beginning before even the instance is not created .This can be done in the
constructor.
========================================================
There are many things that a constructor might do.
or example if we were creating some sort of object that engages in networking we could validate that
a networking connection can be made if we were creating an object that can communicate with the server
to do things like start restart shutdown etc. we might begin by pinging the server to make sure that
it's up and running if our object's purpose was to parse a data file like an SML or CXXVI file.
It might initialize itself by parsing the file and seeing if it is in the proper format.

Any steps that need to be taken before an instance can be used.
We would take care of in the constructor.
- check server is ping

======================================================
__init__ is a keywords variable:it is must be named init
-It is  method automatically called when a new instance is constructed.
- IF it is not present it is not called.
-The self argument is the first appearance of the instance
-__init__ offers the opportunity to initialize attributes in the instance at the time of construction.


"""


class MyNum():
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment(self):
        self.val = self.val + 1


i = MyNum(4)
i.increment()
print(i.val)


