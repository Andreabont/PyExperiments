from decimal import *
from cfraction import *
getcontext().prec = 3
c = generateContinuedFraction(Decimal("3.245"), 10)
print(c)
