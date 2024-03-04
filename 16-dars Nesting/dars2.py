#developer = {
#    'ali':['python', 'c++'],
#    'vali':['html', 'c#'],
#    'soli':['php', 'sql'],
#    'gani':['python','php'],
#    'husan':['c++','c#']
#}
#for ism, tillar in developer.items():
#    print(f"{ism.upper()} quyidagi dasturchilar shu tillarni ishlatadi. ")
#    for til in tillar:
#        print(til.title(), end=" ")
                   #
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())