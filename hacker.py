SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

message = input("Enter the message you want to hack: ")

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = (num - key) % len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
    print(f"{key}: {translated}")