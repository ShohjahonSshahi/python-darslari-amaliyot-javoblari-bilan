#def tub_sonlar(sonlar):
#    """Tub sonlarni chiqaruvchi Funksiya"""
#    x = input("Birinchi sonni kiriting: ")
#    y = input("Ikkinchi sonni kiriting: ")
#    x = int(x)
#    y = int(y)
#    sonlar  = []
#    for m in range(x,y):
#        sonlar.append(m)
#    return sonlar        
#talaba = tub_sonlar(4)
#print(f"{talaba}")

"""
18/12/2020

Dasturlash asoslari

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def tub_sonlar_top(min, max):
    min = input("Birinchi sonni kiriting: ")
    max = input("Ikkinchi sonnni kiriting: ")
    min = int(min)
    max = int(max)
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar

son = tub_sonlar_top(5,100)
print(f"{son}")