car0 = {'modeli': 'gentra',
        'rangi':'oq',
        'yili': 2010,
        'narx':13000,
        'km':20000,
        'karobka':'avtomat',
        }
car1 = {'modeli': 'cobalt',
        'rangi':'qizil',
        'yili': 2011,
        'narx':14000,
        'km':29000,
        'karobka':'mexanik',
        }
car2 = {'modeli': 'lacetti',
        'rangi':'qora',
        'yili': 2022,
        'narx':13050,
        'km':19630,
        'karobka':'avtomat',
        }
#car = car2
#print(f"{car['modeli'].title()},"
#      f"Rangi {car['rangi']}, "
#      f"{car['yili']}-yil, {car['narx']}$")
#cars = [car2, car0, car1]
#for car in cars:
#print(f"{car['modeli'].title()}, "
#      f"Rangi {car['rangi']}, "
#      f"{car['yili']}-yil, {car['narx']}$")
#print(cars[2]['modeli'])
malibus = []
for n in range(10):
    cardr = {'model': 'malibu',
        'rang':None,
        'yil': 2024,
        'narx':None,
        'km':0,
        'karobka':'avtomat',
        }
    malibus.append(cardr)
#    print(malibus)
for malibu in malibus[:3]:
    malibu['rang']='qizil'
for malibu in malibus[3:6]:
    malibu['rang'] = 'oq'
for malibu in malibus[6:]:
    malibu['rang'] = 'qora'
    malibu['karobka'] = 'mexanik'
for malibu in malibus:
    if malibu['karobka'] == 'avtomat':
        malibu['narx'] = 40000
    else:
        malibu['narx'] = 35000
for malibu in malibus:
    print(malibu)