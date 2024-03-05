def kopaytma(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma
print(kopaytma(10,502))
print(kopaytma(10,502,154))
print(kopaytma(10,502,10))