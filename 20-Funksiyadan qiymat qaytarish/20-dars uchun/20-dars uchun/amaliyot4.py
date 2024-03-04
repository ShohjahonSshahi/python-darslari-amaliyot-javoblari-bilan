def aylana(radius, pi=3.14):
    radius = input("Radiusni qiymatini kiriting")
    radius = int(radius)
    aylanaqiymatlari = {
        'radius': radius,
        'diametr': 2*radius,
        'yuz': pi * radius  ,
        'primetr': 3 * radius * 2
    }
    return aylanaqiymatlari
        

qiymat = aylana('radius')
print(f"Aylananig qiymatlari {qiymat} ")
