def katta_son_qaytar(son1, son2, son3):
    """"Uchta son qabul qilib eng kattasini konsolga chiqaruvchi funksiya"""
    son1 = input("Birinchi sonni kiriting: ")
    son2 = input("Ikkinchi sonni kiriting: ")
    son3 = input("Uchinchi sonni kiriting: ")
    max = son1
    if son2 >=max:
        max = son2
    if son3>= max:
        max = son3
    return max
qiymat = katta_son_qaytar(['son1'],['son2'],['son3'])
print({qiymat})


