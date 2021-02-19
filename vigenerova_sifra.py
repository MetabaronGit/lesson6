word = input("Zadej slovo: ").lower()
password = input("Zadej heslo: ").lower()
password_index = 0
encrypted_word = str()

# ord() a=97 - z=122 (a je posun o 1)
SHIFT_CONST = 96
for word_char in word:
    char_shift = ord(password[password_index]) - SHIFT_CONST
    shifted_char = ord(word_char) + char_shift
    if shifted_char > ord("z"):
        shifted_char -= 26 #počet znaků malé abecedy v ASCII
    encrypted_word += chr(shifted_char)
    password_index += 1
    if password_index > len(password) - 1:
        password_index = 0

print(f"Zašifrované slovo je: {encrypted_word}")


# vzorove řešení
# zadání vstupu
vstup = input("Zadejte text k zašifrování: ")
heslo = input("Zadejte heslo: ")
vystup = ""
# průchod všemi znaky ve vstupu
for i, znak in enumerate(vstup):
    # výpočet posunu v abecedě
    x = ord(heslo[i % len(heslo)]) - (ord("a") - 1)
    # ošetření přeteční přes z
    if ord(znak) + x > ord("z"):
        x -= ord("z") - ord("a") + 1
    # získání transformovaného znaku
    vysledek = chr(ord(znak) + x)
    # přidání znaku do výstupu
    vystup += vysledek
print("Výsledek:", vystup)
input()