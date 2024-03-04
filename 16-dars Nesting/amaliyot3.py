davlatlar = {
    "o'zbekiston":{'poytaxt':'toshkent',
                   'aholisi':33_000_000,
                   'maydon':448978,
                   'pul birligi':"so'm"},
    "rossiya":{'poytaxt':'moskva',
                   'aholisi':144_000_000,
                   'maydon':17_098_246,
                   'pul birligi':"rubl"},
    "amerika":{'poytaxt':'washington',
                   'aholisi':327_000_000,
                   'maydon':9_631_948,
                   'pul birligi':"dollar"},
    "malaysiya":{'poytaxt':'kuala-lampur',
                   'aholisi':25_000_000,
                   'maydon':329750,
                   'pul birligi':"rinngit"},
}
for name,info in davlatlar.items():
    if name.lower()== "amerika":
        name = name.upper()
    else:
        name = name.capitalize()
    print(f" {name.upper()}ning poytaxti  {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']}"
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi: {info['pul birligi'].upper()}")