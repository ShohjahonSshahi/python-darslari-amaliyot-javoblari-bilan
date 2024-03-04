print("BU Muzeyga chipta sotib polish uchun ishlatiladigan dastur!")
yosh = "Yoshingizni kiriting"
yosh += "(Dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing) "
#ishora = True
while True:
    qiymat = input(yosh)
    if qiymat == 'exit' or qiymat == 'quit':
        break

    qiymat = int(qiymat)
    if qiymat<=7:
        print("Sizga kirish 2000 so'm")
    elif qiymat>7 and qiymat<=18:
        print("Sizga kirish  3000 so'm")
    elif qiymat>18 and qiymat<=65:
        print("Sizga kirish 10000 ming So'm")
    elif qiymat>65:
        print("Sizga kirish 0 So'm")
print("Dastur tugadi!")
        
