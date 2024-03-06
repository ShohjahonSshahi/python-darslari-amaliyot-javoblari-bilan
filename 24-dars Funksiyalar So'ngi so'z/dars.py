import math
#def nom(argument):
#    return ifoda
#lambda argument:ifoda
uzunlik = lambda pi, r: 2*pi*r
print(uzunlik(math.pi,10))
kvadrat = lambda x, y:x**y
print(kvadrat(3,3))

                          #
def daraja(n):
    return lambda x: x**n 
kvadrat  = daraja(2)
print(f"{kvadrat(3)}")
                         #
from math import sqrt
sonlar = list(range(0,11))
ildizlar = list(map(sqrt,sonlar))
#print(ildizlar)
                                                                                        #
def daraja2(x):
    return x*x
print(list(map(daraja2,sonlar)))
                  #
kvadratlar = list(map(lambda x:x*x, sonlar))
print(kvadratlar)