def talaba_info(ism,familiya,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba = talaba_info('Shohjahon','Boymurodov', yili=2004, yosh=20, otasining_ismi='Palonchayevich')
tala1 = talaba_info('Umid','Ergashev', yili=2004, otasining_ismi='Palonchayevich')
print(talaba)
print(tala1)