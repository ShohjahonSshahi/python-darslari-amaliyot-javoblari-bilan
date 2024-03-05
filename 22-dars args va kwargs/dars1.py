def summa(x, y, *sonlar):
    """Kiritilgan sonlarning yig'indisini hisoblaydigan Funksiya"""
    return x+y+sum(sonlar)

print(summa(10,502))
print(summa(10,502,154))
print(summa(10,502,10))
print(summa(10,50,10,2001))