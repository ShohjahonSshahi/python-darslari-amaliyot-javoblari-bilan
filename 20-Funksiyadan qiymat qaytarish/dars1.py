def avto_info(kompaniya, yili, karobka, model, rangi, narxi=None):
    avto ={'kompaniya':kompaniya,
           'model':model,
           'yili':yili,
           'karobka':karobka,
           'rang':rangi,
           'narxi':narxi
           }
    return avto
avto0 = avto_info('Gm',2023,'mexanik','molibu','qizil')
avto1 = avto_info('gm',2018,'avtomat','cobalt','oq', 13250)
avtolar = [avto0,avto1]
print(f"Onlayn bozordagi mavjud mashinalar")
for avto in avtolar:
    if avto['narxi']:
        narx = avto['narxi']
    else:
        narx = 'Nomalum'
    print(f"{avto['kompaniya']} kompaniyasi, {avto['rang']} rangli {avto['model']} mashinasining  narxi {narx} $$$")