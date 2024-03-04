talabalar = ['hasan', 'umid','ali','soli','husan','tohir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi.")
    baholangan_talabalar[talaba] = int(baho)

#print(baholangan_talabalar) #Lugatni elementlarini korish uchun shu qatordagi birinchi #ni ochiring
print(talabalar)  #Ruyxatda elementlar qolmaganini ko'rish mumkin, bunig uchun birinchidagi # ni o'chiring
    