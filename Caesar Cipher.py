
FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_shift(message, shift, mode):
    result = ""

    # Go through each of the letters in the message
    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            if mode == "encrypt":
                new_char_code = char_code + shift
            elif mode == "decrypt":
                new_char_code = char_code - shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    print(result)

def get_mode():
    while True:
        mode = input("Choose the mode (encrypt/decrypt): ").lower()
        if mode in ["encrypt", "decrypt"]:
            return mode
        else:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")

print()
print("*** CAESAR CIPHER PROGRAM ***")
print()

user_message = input("Message: ")
user_shift_key = int(input("Shift Key (integer): "))
mode = get_mode()

caesar_shift(user_message, user_shift_key, mode)
