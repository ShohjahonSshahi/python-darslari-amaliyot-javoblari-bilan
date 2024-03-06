import random as r
sonlar = r.sample(range(100),10)
print(sonlar)
def juftmi(x):
    return x%2==0
juft_sonlar = list(filter(juftmi,sonlar))
print(juft_sonlar)
juft_sonlar = list(filter(lambda x:x%2==0,sonlar))
print(juft_sonlar)