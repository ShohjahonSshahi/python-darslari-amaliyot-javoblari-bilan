def toliq_ism_yasa(ism, familiya):
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism

talaba = toliq_ism_yasa('Ali', 'Ergashev')
talaba1 = toliq_ism_yasa('umid', 'alijonov')
talaba2 = toliq_ism_yasa('soli','ganiyev')
print(f"Darsga kelmagan talabalar: {talaba.title()}, {talaba1.title()}, "
      f"Darsga {talaba2.title()} kechikib keldi.")