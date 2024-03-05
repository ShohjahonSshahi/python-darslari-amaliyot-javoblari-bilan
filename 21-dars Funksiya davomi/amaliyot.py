
def katta_harf(matnlar):
    """ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya"""
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()   

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)



