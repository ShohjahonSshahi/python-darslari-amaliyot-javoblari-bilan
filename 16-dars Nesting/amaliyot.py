shaxs0 = {'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
        'yil':810,
        'manzil': 'Buxoro',
        'umr':60
        }
shaxs1 = {'ism': 'Abdulla Qodiriy',
        'yil':1894,
        'manzil': 'Toshkent',
        'umr':44
        }
shaxs2 = {'ism': 'Erkin Vohidov',
        'yil':1936,
        'manzil': "Farg'ona",
        'umr':80
        }
shaxs3 = {'ism': 'Alisher Navoiy',
        'yil':1441,
        'manzil': 'Hirot',
        'umr':60
        }
shaxs4 = {'ism': 'shomurodov shohjahon',
        'yil':2004,
        'manzil': 'samarqand',
        'umr':'Hali tirik'
        }
shaxs = [shaxs0,shaxs1,shaxs2,shaxs3,shaxs4]
for shax in shaxs:
    print(f"{shax['ism'].title()}, "
          f"{shax['yil']}-yilda tug'ilgan, "
          f"{shax['manzil']}da yashagan  "
          F"{shax['umr']} yil umr ko'rgan")
