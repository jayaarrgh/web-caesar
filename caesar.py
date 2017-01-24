def encrypt(text, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    msg = ''
    for i in text:
        if i not in alphabet and i not in ALPHABET:
            msg += i
        elif i in alphabet:
                if rotate_character(i, rot) < 26:
                    msg += alphabet[rotate_character(i, rot)]
                else:
                    msg += alphabet[rotate_character(i, rot)%26]
        else:
            if rotate_character(i, rot) < 26:
                msg += ALPHABET[rotate_character(i, rot)]
            else:
                msg += ALPHABET[rotate_character(i, rot)%26]
    return msg

def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in alphabet:
        char_val = alphabet.index(letter)
    else:
        char_val = ALPHABET.index(letter)
    return char_val

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotamt = alphabet_position(char) + rot
    return rotamt