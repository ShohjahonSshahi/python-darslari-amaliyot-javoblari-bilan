def talaba_haqida_malubot_ber(ism, familiya, t_yil,t_joy,email,tel_raqam=None):
    malumot = {
        'ism': ism,
        'familiya' :familiya,
        't_yil' : t_yil,
        't_joy':t_joy,
        'email': email,
        'tel_raqam':tel_raqam
    }
    return malumot
#talaba = talaba_haqida_malubot_ber('Asilbek', 'Abdullayev', 2004, 'Samarqand', 'emailimyuq')
#talaba1 = talaba_haqida_malubot_ber('Umid', 'Ergashev', 2004, 'Samarqand', 906547895121)
#talabalar = [talaba, talaba1]

#print(talabalar[0]['familiya'])

print('Kelajakdagi bulajak ishchilarni kiriting:')
ishchilar = []
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    t_yil = input("To'g'ilgan yilini kiriting: ")
    t_joy = input("To'g'ilgan joyini kiriting: ")
    email = input("Email manzilini kiriting: ")
    tel_raqam = input("Telefon raqamini kiriting:")
    ishchilar.append(talaba_haqida_malubot_ber(ism, familiya, t_yil,t_joy,email,tel_raqam)) 
    javob = input("yana davom etasizmi (HA yoki YO'Q deb yozing!!!): ")
    if javob == "YO'Q":
        break
print(" Bo'lajak Ishchilar:")
for ishchi in ishchilar:
    print(
        f"{ishchi['ism'].title()} {ishchi['familiya'].title()}, {ishchi['t_yil']}-yilda tug'ilgan."
        f"{ishchi['t_joy'].title()} viloyati. {ishchi['email'].title()} email manzili. Telefon raqami {ishchi['tel_raqam']} "
    )