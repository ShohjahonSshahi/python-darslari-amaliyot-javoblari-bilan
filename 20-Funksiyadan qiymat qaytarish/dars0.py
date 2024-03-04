def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya} "
    return toliq_ism.title()
talaba = toliq_ism_yasa('olim','fattoyev','abrorivich')
talaba1 = toliq_ism_yasa('husan','fattoyev')
print(f"Darsga kelmagan talbaar {talaba.title()} va {talaba1.title()}")