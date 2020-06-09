"""
-instance methods are variables defined in the class
-They are  accessed through hte instance.instance.method()
-When called through the instance the instance is automatically passed as the first argument to the method.
-Because of this automatic passing of the instance  instance methods are known as bound method
i.e bound to the instance upon which it is called.

"""


class CallMe(object):
    def callme(self):     # if you remove the self keywords than got error
        print("This is call me function by Instance")
        print(self)


this_callme = CallMe()
this_callme.callme()  # By default this_callme instance  pass the 1 argument that is reference  or id that an instance
# of function OR
# rule when we call a method on an instance the instance gets passed as the first argument  automatically.
print(this_callme)


# how instance methods can be used to modify the data stored in the instance

