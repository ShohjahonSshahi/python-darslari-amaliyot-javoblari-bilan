print("Mahsulotlar ro'yxatini tuzamiz:")
mahsulotlar = []
n = 1
while True:
    savol = f"{n}-mahsulotni nomini kiriting."
    mahsulot = input(savol)
    mahsulotlar.append(mahsulot)
    takrorlash = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
    n += 1
    if takrorlash == "yo'q":
        break

print("Mahsulotlaringizni ro'yxati: ")
for mahsulot in mahsulotlar:
    print(f"{mahsulot.title()}")
#print(mahsulotlar)
bozor  = {}
while mahsulotlar:
    narsa = mahsulotlar.pop()
    narx = input(f"{narsa.title()}ni narxini kiting: ")
    print(f"{narsa.upper()} baholandi.")
    bozor[narsa] = int(narx)
for mahsulot, narx in bozor.items():
    print(f"{mahsulot.title()}ning,  narxi {narx} so'm.")
    

#print(bozor)
    