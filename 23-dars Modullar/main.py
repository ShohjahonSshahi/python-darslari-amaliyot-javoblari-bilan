#import avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz

#avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#avto_info_mod.info_print(avto1)
                #
#import avto_info_mod as shoh # avto_info_mod ni qisqa nom aim bilan chaqiramiz

#avto1 = shoh.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#shoh.info_print(avto1)
                                       #
#from avto_info_mod import avto_info, info_print # Modulning ichidagi funksiyalarni caqiriqb olish. FROM ya'ni DAN deb tarjima qilinadi!!! 

#avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#info_print(avto1)
                                         #
#from avto_info_mod import avto_info as bosh, info_print as hosh

#avto1 = bosh("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#hosh(avto1)
                                                #
from avto_info_mod import *       #MOdulning uchudagi hamma funksiyalarni chaqirib oladi

avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)
                                               