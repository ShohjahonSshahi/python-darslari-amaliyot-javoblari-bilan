#talaba = {
#    'ism':'Ali',
#    'familiya':'Sattarov',
#    'yosh': 20,
#    'fakultet':'MOl BOqish',
#    'kurs':2
#  }
#print(talaba.items())
#for l,b in talaba.items():
#    print(f"Kalit: {l}")
#    print(f"Qiymat: {b}")
#for k,l in talaba.items():
#    print(f"{k.upper()}i {l}")

#print(talaba.keys())
#print('Ruyxatdagi Kalitlar: ')
#for mak in talaba:
#    print(f'{mak.upper()}')
#bozorlik = ['uzum','olma','shaftoli','non','un','telefon','blutus']
mahsulotlar = {'olma':10000,
               'shaftoli':15000,
               'banan': 20000,
               'non':3000,
               'un':250000,
               'uzum':26312,
               'telefon':140000,
               'sdcfsd':140000,
               'zcsdjcnsd':20000}

#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
 #       print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")
#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos, Dokoningizga {buyum}ni olib keling!")
                                                #
#print("Do'konimizdagi mahsulotlat=r: ")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot)
                              #
print("Mahsulotlarning narxi quyidagicha: ")
for narx in set(mahsulotlar.values()):
    print(narx)
                                        #
