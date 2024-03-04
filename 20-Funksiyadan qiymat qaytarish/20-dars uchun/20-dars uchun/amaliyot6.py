#def fibonachchi(son):
#    """Foydalanuvchidan son qabul qilib uni fibonachchi ketma-ketligiga chiqaruvchi Funksiya"""
#    fibonachchi_ketma_ketligi = []
#    son = input("Xoxlagan birorta son kiriting: ")
#    son = int(son)
#    n = 0
#    fibonachchi_ketma_ketligi.append(n)
#    fibonachchi_ketma_ketligi[0] = n
#    son = son + 0
 #   fibonachchi_ketma_ketligi.append(son)
 #   fibonachchi_ketma_ketligi[1] = son
 #   fibonachchi_ketma_ketligi[0] + fibonachchi_ketma_ketligi[1] == fibonachchi_ketma_ketligi[3]
#    return fibonachchi_ketma_ketligi
#sonlar = fibonachchi(23)
#print(f"{sonlar}")

def fibonacci(n):
    sonlar = []
    n = input("Xoxlagan biror sonni kiriting: ")
    n = int(n)
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar

sonlar = fibonacci(1)
print(f"{sonlar}")
#print(fibonacci(10))
