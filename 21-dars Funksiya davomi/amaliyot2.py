def katta_harf(matnlar):
    """ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya"""
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar   


ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)