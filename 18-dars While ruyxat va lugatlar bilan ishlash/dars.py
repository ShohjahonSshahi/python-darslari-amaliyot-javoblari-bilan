print("Yaqin do'stlaringizni ro'yxatini tuzamiz. ")
ismlar = []
n = 1
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
    n += 1
    if takrorlash == "yo'q":
        break

print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(f"{ism.title()}")
print(ismlar)