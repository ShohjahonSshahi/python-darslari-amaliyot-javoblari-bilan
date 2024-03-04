print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")

savol = "Musbat son kiriting: "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'stop' or qiymat == 'quit':
        break
    qiymat = int(qiymat)
    if qiymat>0:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("Siz dasturni tugata oldingiz😁")