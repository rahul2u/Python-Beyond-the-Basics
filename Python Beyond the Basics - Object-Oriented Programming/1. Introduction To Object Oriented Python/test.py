# import 3 ways
import mymod   # mymod there is called namespace
from mymod import var
from mymod import myfunction
import mymod as mm

print(mm.var)
mm.myfunction()

print(var)
myfunction()

# class name always uppercase .This is standard convention
from decimal import Decimal  # first is module name that is lower d and Decimal is class
print(Decimal('3.5') + Decimal('3.5'))

# a module is just a file that contains Python code and a class is simply Python code.

