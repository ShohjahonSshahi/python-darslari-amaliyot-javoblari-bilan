mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan",'alvolir','alchor','adebur','asebur','aolur']

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)
mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)

#PASTDAGI KOdda RUYXATDAGI ELEMENTLARNING a HARFI BILAN BOSHLANADIGAN VA r HARFI BILAN TUGAYDIGAN ELEMENTLARNI BITTA RUYXATGA JOYLAYDI!!!
javob = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(javob) 