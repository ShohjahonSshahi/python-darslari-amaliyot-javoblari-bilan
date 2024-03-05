def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=int(baho)
    return baholar

talabar = ['ali','vali','hasan','husan']
baholar = bahola(talabar)
print(baholar)