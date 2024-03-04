dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingizni ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()}ning,  Yoshi {yosh} da.")
print(dostlar)