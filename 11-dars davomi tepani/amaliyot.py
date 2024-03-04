                      #Amaliyot-1
#son1 = int(input("Birinchi sonni kiriting: "))
#son2 = int(input("Ikkinchi sonni kiriting: "))
#if son1%2:
#    print('Bu juft son emas')
#else:
#    print('rahmat')
                           #Amaliyot-2
#yosh = int(input("Yoshingiz nechida: "))
#if yosh<4 or yosh>60:
#    narx = 0;
#elif yosh<18:
#    narx = 10000;
#else:
#    narx = 20000;
#print(f"Sizga kirish {narx} so'm")
     
                                         #Amaliyot-3
#son1 = int(input("Birinchi sonni kiriting: "))
#son2 = int(input("Ikkinchi sonni kiriting: "))
#if son1 == son2:
#    print(f"{son1}={son2}");
#elif son1>son2:
#    print(f"{son1}>{son2}");
#else:
#    print(f"{son1}<{son2}")
                                     #Amaliyot-4

#mahsulotlar = ['olma','qalam','fonar','lampochka','chelak','asal','choy','nok','non','telifon',]
#savat = []
#for s in range(6):
#    savat.append(input(f"{s+1}-Savatga mahsulot kiriting: "))
   # print(savat)

#for tovar in savat:
#    if tovar in mahsulotlar:
#        print(f"Do'konimizda {tovar} bor")
#    else:
#        print(f"Do'konimizda {tovar} yo'q")
                                    #amaliyot-5
#mahsulotlar = ['olma','qalam','fonar','lampochka','chelak','asal','choy','nok','non','telifon',]
#savat = []
#for n in range(3):
 #   savat.append(input(f"Savatga {n+1} mahsulotni kiriting: "))
   # print(savat)

#bor_mahsulotlar = []
#mavjud_emas = []
#for tovar in savat:
#    if tovar in mahsulotlar:
#        bor_mahsulotlar.append(tovar)
#    else:
#        mavjud_emas.append(tovar)

#if mavjud_emas:
#    print(f"Do'konimizda quyidagi mahsulotlar yo'q: ")
 #   for tovar in mavjud_emas:
  #      print(mahsulotlar)
#else:
 #   print("Siz so'ragan barcha mahsulotlar do'konimmizda bor")
                     #Amaliyot-6
#foydalanuvchilar = ["ali","Soli","Vali","yanvar","narz","umar"]
#foydalanuvchi = input("Yangi login kiriting:")
#if foydalanuvchi in foydalanuvchilar:
#    print("BU LOGIN MAVJUD YANGI LOGIN KIRITING")
#else:
#    print(f"Xush kelibsiz, {foydalanuvchi.title()}")
                              #Amaliyot-7
son = int(input("Biror bir son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
   