"""
class: A blueprint of instance
        or
        classes define an the instance blueprints.
Instance : a constructed object of class
Type: indicates the class the instance belong to
Attributes: any object value : object.attributes (data and method both are attributes,method is callable attributes)
Method : a callable attributes define in class
           OR
           similar function but it define with in class and access using the instance or object
object : combined data and functionality
            OR
            a unit of  data with  associated functionality
how to check the all attributes of objects
    ex val =10
       print(dir(val))

var = 'hello'
    - what is var type
             it is string class and that is type of string
             we can also called a string object or a string object


=================================================================
instance Methods and attributes
- A car can be seen as a class of  object
-The car class provides the blueprint for a car object
- Each instance of a car does the same things(method(functionality,behaviour))
-But each car instance has its own states(attributes)

-difference between the blueprint which is defined in the class or the
 factory and the state of each instance which is defined by its use.

- data can only processing by method(change ,rename etc)
-Method's often change an instance's state(its data)

========================================================================
Defining A Class And Constructing an Instance
Review:
    Classes are instance factories
    Classes define an "instance blueprint"

Construct an instance or object of the class
    Instance known to which class they belong(type)
    Instance can access variables defined in the class


==============================================================
6 points to understanding Classes Mechanics
or
 six points that you want to absorb in order to understand how classes work.

1- An instance of a class  knows what class its form
2-Vars define in class avalible to the instance
3- A method on a instance passes instance as the first argument to the method(named self in the method)
4-Instances have their own data called instance attributes
5-variables defined in class  are called the class attributes
6-When read an attribute python look for it first in instance and then in class.



"""


class MyClass(object):
    pass


class MyClassWithValue(object):
    vars = 10


this_object = MyClass()
print(this_object)         # print the hexcode of the object, where is created in memory

that_object = MyClass()
print(that_object)


this_object_with_value = MyClassWithValue()
print(this_object_with_value.vars)

