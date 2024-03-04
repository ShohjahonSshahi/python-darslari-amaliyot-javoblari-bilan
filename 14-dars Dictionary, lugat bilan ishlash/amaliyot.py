#akam = {'ism': 'Ogabek', 'yil': 2009, 'manzil':'Samarqand', 'fakultet':'mol boqishni urganamiz' }
#print(f"{akam['fakultet'].title()} Fakultetida o'qiydi, Ismi {akam['ism'].title()}, {akam['yil']}-da tugilgan, {akam['manzil'].title()} da yashaydi")

                      #Amaliyot-2
#taomlar = {'otam':'osh','onam':'somsa','akam':'shorva','singlim':'manti'}
#print(f"Otamning sevimli taomi {taomlar['otam'].title()}\n Onamning sevimli taomi {taomlar['onam'].title()}\n Akamning sevimli taomi {taomlar['akam'].title()},\n Singlimning sevimli taomi {taomlar['singlim'].title()}")
                           #Amaliyot-3
#p_izohliL = {'integer':'butun son','string':'harflar','float':'onli son','if':'agar','else':'aks holda','for':'uchun','in':'ichida'}
#tarjim = input("Biror soz kiting: ").lower()
#print(p_izohliL.get(tarjim, 'Bunday soz mavjud emas'))
                         #Amaliyot-4
p_izohliL = {'integer':'butun son','string':'harflar','float':'onli son','if':'agar','else':'aks holda','for':'uchun','in':'ichida'}
keyyo = input("Biror soz kiting: ").lower()
tarjima = p_izohliL.get(keyyo)
if tarjima== None:
    print(' Ruyxatda BUnday soz mavjud emas'),
else:
    print(f'Siz suragan soz {tarjima.upper()} deb tarjima qilinadi')
#print(p_izohliL.get(tarjim, 'Bunday soz mavjud emas'))
