import pyperclip

SYMBOLS = "ABCDEFGHIKJLMNOPQRSTUVWXYZ"

while True:
    prompt = input("Enter e to encrypt or d to decrypt: ").lower()
    if prompt == "e" or prompt == "d":
        mode = prompt
        break
    print("Enter e or d")

while True:
    max_key = len(SYMBOLS) - 1
    prompt = input(f"Enter key between 0 to {max_key}: ")
    if prompt.isdecimal() and int(prompt) in range(len(SYMBOLS)):
        key = int(prompt)
        break

message = input("Enter your message: ").upper()
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "e":
            num = (num + key) % len(SYMBOLS)
        else:
            num = (num - key) % len(SYMBOLS)
        translated += SYMBOLS[num]
    else:
        translated += symbol

print(translated)
try:
    pyperclip.copy(translated)
    print("Your text has been copied to clipboard")
except:
    pass