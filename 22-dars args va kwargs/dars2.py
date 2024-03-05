def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
print(avto2)
