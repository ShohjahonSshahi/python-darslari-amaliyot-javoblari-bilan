import random as r
# randint BERILGAN ORALIQDAGI SONNI TASODIFIY QILIB QAYTARADI
son  = r.randint(0,100)
print(son)

# .choice() BU FUNKSIYA BIROR BIR RO'YXATNING ICHIDAN BIROR BIR MATNNI TANLAB OLADI
ismlar = ['ali','vali', 'soli','gani']
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))

x = list(range(0,51,2))
print(x)
print(r.choice(x))

# .shuffle() BU FUNKSIYANING VAZIFASI ARALASHTIRIB TASHLASH
X = list(range(10,100))
r.shuffle(x)
print(x)