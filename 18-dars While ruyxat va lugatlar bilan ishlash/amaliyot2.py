dostlar = {}
while True:
    ism = input("Do'stingizni ismini kiriting:")
    yosh = input("Do'stingizni yoshini kiriting: ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ism kiritasizmi(ha yoki yo'q deb javob qaytaring!!!): ")
    if javob != "ha":
        break
for ism, yosh in dostlar.items():
    print(f"{ism.upper()}ning yoshi, {yosh}da!")