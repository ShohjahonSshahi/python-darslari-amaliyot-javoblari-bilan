import random
from names import ismlar

def get_word():
    word = random.choice(ismlar)
    while "-" in word or ' ' in word:
        word = random.choice(ismlar)    
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Men {len(word)} xonali ism O'yladim. Topa olasizmi?")
    # print(word)
    while word_letters:
        print(display(user_letters,word))
        if user_letters:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
        
        letter = input("Xarf kiritimg: ").upper()
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting.")
            continue        
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} xarf to'g'ri.")
        else:
            print("Bunday harf yo'q.")
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta o'rinish bilan topdingiz.")

print(play())