def oraliq(min,max,qadam=1):
    sonlar = []
    while min<max:
        sonlar.append(min)
        if qadam:
            qadam = min + qadam
        else:
            qadam = ""
        min += 1
    return sonlar

print(oraliq(12,23,3))
print(oraliq(23,34,3))
print(list(range(23,34,3)))