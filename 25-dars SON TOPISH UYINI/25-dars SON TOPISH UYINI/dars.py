import random
def sontop(x=10):
    tasodifiy_son  = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while  True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            break
    print(f"Tabriklaymiz Siz sonni {taxminlar} urinish bilan  topdingiz!")
    return taxminlar
   

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi_chegara = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi_chegara != yuqori:
            taxmin = random.randint(quyi_chegara,yuqori)
        else:
            taxmin = quyi_chegara
        javob = input(f"siz {taxmin} sonni o'yladingiz: to'g'ri (t) ,"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi_chegara = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar
def play(x=10):
    yana_uyin = True
    while yana_uyin:
        taxminlar_user =sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim")
        elif taxminlar_user< taxminlar_pc:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        yana_uyin = int(input("Yana o'ynaysizmi/ ha(1)/yo'q(0):"))

print(play())


