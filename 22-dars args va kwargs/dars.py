def summa(*sonlar):
    """Kiritilgan sonlarning yig'indisini hisoblaydigan Funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(10,502))
print(summa(10,502,154))
print(summa(10,502,10))
print(summa(10,50,10,2001))