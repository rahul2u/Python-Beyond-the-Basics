"""
how to decide which data put in class this is decide when we put and decide the 
   Or
How to work object and class data and access
"""
val = 10  # global variable can not used in the class so we need to define in the class


class MyClass(object):
    count = 0
    
    def __init__(self, value):
        self.val = value
        MyClass.count += 1
               cccccccccccc
    def set_val(self, new_value):
        try:
            value = int(new_value)
        except ValueError:
            return
        self.val = new_value

    def get_val(self):
        return self.val

    def get_count(self):
        return MyClass.count


a = MyClass(10)
b = MyClass(50)
c = MyClass(100)

for i in (a, b, c):
    print("val of object", i.get_val())
    print("Count",i.get_count())











