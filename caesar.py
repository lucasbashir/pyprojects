import pyperclip

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_mode():
    while True:
        prompt = input("Press e to encrypt and d to decrypt: ").lower()
        if prompt == "e" or prompt == "d":
            return prompt
        print("Enter e or d")


def get_key():
    while True:
        max_key = len(SYMBOLS) - 1
        prompt = input(f"Enter key from 0 to {max_key}: ")
        if prompt.isdecimal() and int(prompt) in range(len(SYMBOLS)):
            return int(prompt)
        print(f"Enter a valid key between 0 and {max_key}")


def get_message(mode):
    prompt = f"Enter the message to {mode}: "
    return input(prompt).upper()


def translate_message(mode, message, key):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            if mode == "encrypt":
                num = (num + key) % len(SYMBOLS)
            else:
                num = (num - key) % len(SYMBOLS)
            translated += SYMBOLS[num]
        else:
            translated += symbol
    return translated


def main():
    mode = get_mode()
    key = get_key()
    message = get_message(mode)
    translated = translate_message(mode, message, key)
    print(translated)
    try:
        pyperclip.copy(translated)
        print(f'Full {mode}ed text copied to clipboard.')
    except:
        pass


if __name__ == '__main__':
    main()
