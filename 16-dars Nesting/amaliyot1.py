shaxs0 = {'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
        'yil':810,
        'manzil': 'Buxoro',
        'umr':60,
        'asar':["Al-jome' as-sahih",
                "Al-adab al-mufrad",
                "Al-tarix al-kabir",
                "Al-tarix as-sag'ir"]
        }
shaxs1 = {'ism': 'Abdulla Qodiriy',
        'yil':1894,
        'manzil': 'Toshkent',
        'umr':44,
        'asar':["O'tgan kunlar",
                "mehrobdan Chayon",
                "Obid Ketmon"]
        }
shaxs2 = {'ism': 'Erkin Vohidov',
        'yil':1936,
        'manzil': "Farg'ona",
        'umr':80,
        'asar':["Tong nafasi",
                "Qo'shiqlarim sizga",
                "O'zbegim",
                "Qiziquvchan matmusa"]
        }
shaxs3 = {'ism': 'Alisher Navoiy',
        'yil':1441,
        'manzil': 'Hirot',
        'umr':60,
        'asar':["Xamsa",
                "Lisonut-Tayr",
                "Mahbub ul-qulub",
                "Munojot"]
        }
#shaxs4 = {'ism': 'shomurodov shohjahon',
#        'yil':2004,
#        'manzil': 'samarqand',
#        'umr':'Hali tirik'
 #       }
shaxs = [shaxs0,shaxs1,shaxs2,shaxs3,]
for who in shaxs:
    ism = who['ism']
    asarlar = who['asar']
    print(f"\n{ism}nig mashkur asarlari:")
    for asar in asarlar:
        print(asar)











#    print(f"{answer['ism'].upper()}ning mashxur asarlari:"
#          f"{kitob['asar']}")
    
#for shohjahon in kitob:
#    print(shohjahon)
    