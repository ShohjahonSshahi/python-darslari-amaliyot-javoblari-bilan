#lugat = {'apple':'olma',
#         'banana':'banan',
#         'mom':'oyi',
#         'dad':'dada',
#         }
#for k,an in sorted(lugat.items()):
#    print(f"{k}-{an}")
                                           #Amaliyot-2
#lugat = {'uzbkiston':'Tashkent',
#         'tojikiston':'bishkek',
#         'argentina':'Buenis ayres',
#         'amerika':'washington',
#         'hindiston':'munbay',
#         'fransiya':'parij',
#         }
#print('Dunyo davlatlari:')
#for davlat in sorted(lugat.keys()):
#    print(davlat.upper())
#    print(davlat)
#print("Poytaxtlar quyidagilar: ")
#for poytaxt in sorted(lugat.values()):
#    print(poytaxt.upper())
#    print(poytaxt)
                         #Amaliyot-3
#ruyxat = {'uzbkiston':'Tashkent',
 #        'tojikiston':'bishkek',
 #        'argentina':'Buenis ayres',
 #        'amerika':'washington',
 #        'hindiston':'munbay',
 #        'fransiya':'parij',
 #        }
#davlat = input("Biror bir davlatni kiriting:")
#poytaxt = ruyxat.get(davlat)

#if poytaxt ==None:
#    print("Kechirasiz, bizda bunaqa ma'lumot yo'q!"),
#else:
#    print(f"{davlat.upper()}ning poytaxti  {poytaxt.title()}")
                                  #Amaliyot-4
menyu = {'choy':3000,
         'somsa':5000,
         'kofe':8000,
         'assorti':10000,
         'shashlik':15000,
         'manti':6000,
         'osh':35000,
         'shorva':25000,
         'non':5000,
         'pepsi':12000,
         }
byurtma = []
print("Byurtmani kiriting:")
for sh in range(5):
    byurtma.append(input(f"{sh+1} taom:"))
for shoh in byurtma:
    if shoh in menyu:
        print(f"Byurtmangiz {shoh.upper()}, {menyu[shoh]}  So'm!")
    else:
        print("Bizda bunday taom yo'q!")
narx = int(menyu[shoh])
print(f"Umumiy narx {sum(narx)} so'm bo'ladi, Byurtmani qabulqildik!")