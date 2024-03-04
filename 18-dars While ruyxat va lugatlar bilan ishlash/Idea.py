print("Talabalar haqida ma'lumotlar shakllantiramiz!!!")
ruyxat = []
n = 1
while True:
    savol = f"{n}-talabaning ismini kiriting:"
    ism = input(savol)
    ruyxat.append(ism)
    print(f"{ism.upper()}ninng ismi qabul qilindi!")
    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q ikkisidan birini kiriting)")
    n += 1
    if takrorlash != 'ha':
        break
print("Ismlar ro'yxati:")
for ism in ruyxat:
    print(f"{ism.title()}")


ism_familiya = {}

while True:
    lol = ruyxat.pop()
    familiya = input(f"{lol.title()}ning Familiyasini kiriting:")
    print(f"{lol.upper()}ninng familiyasi qabul qilindi!")
    ism_familiya[lol] = (familiya)
    #    Mana shu yerda xatolik bor 
    print("Iism familiyalar ruyxati:")
    for ism, familiya in ism_familiya.items():
        print(f"{ism.title()}ning,  familiyasi {familiya.upper()}.")




    

    