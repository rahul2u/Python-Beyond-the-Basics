"""

-A paradigms(pronounce as 'paradim' ) for code organization and design. or organizing your code
-The oops paradigms
    1-Organize data into objects and functionality into methods
    2-Define object specification (data and method ) in classes
-Promote code collaboration, code extension and maintenance
- This primary paradigms for software worldwide.
- All programs are compromised of code that's designed to process to data.
-Store the data temporary in variables and process the data and the we call the
function process the the variables.

-The object oriented paradigms organize the data in specially design entity called object and functionality
for processing the the data into the specialized functions that call methods.

-The design the of these objects and methods is specified in a kind of a blue print which we called a class .

- This paradigms is one of the most important advance in software design.
- Using the class we use own custom type object but not possible .
- functionlity  and data is connect.

"""
# Procedural Programing and Object oriented programing increment a variable

# Procedural


def increment_variable(increment):
    increment = increment + 1
    return increment


print(increment_variable(2))


# object oriented programing to increase the variables
class IncrementVaraible(object):
    def __init__(self):
        self.val = 0

    def increment(self):
        self.val = self.val + 1

    def 








