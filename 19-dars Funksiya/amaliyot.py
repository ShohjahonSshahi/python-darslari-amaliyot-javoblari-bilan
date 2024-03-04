def bolinish_belgilari(son):
    """BU funksiya sonlarning 1dan ungacha bulinish belgilarini tekshiradio"""
    for m in range(1,11):
        if not son%m:
            print(f"{son}  {m} ga bo'linadi!!!")
        else:
            print(f"{son} {m}ga bolinmaydi")
bolinish_belgilari(70)
bolinish_belgilari(65)