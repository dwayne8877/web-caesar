def alphabet_position(letter):

    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
    upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if letter in lower_alpha:
        return lower_alpha.index(letter)

    if letter in upper_alpha:
        return upper_alpha.index(letter)

def rotate_character(char, rot):

    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char_return = ''


    if char not in lower_alphabet and char not in upper_alphabet:
        if char == ' ':
            char_return = ' '
        else:
            char_return = char


    if char in upper_alphabet:
        rotated_index = upper_alphabet.index(char) + rot
        if rotated_index < 26:
            char_return = upper_alphabet[rotated_index]
        else:
            char_return = upper_alphabet[rotated_index % 26]
    if char in lower_alphabet:
        rotated_index = lower_alphabet.index(char) + rot
        if rotated_index < 26:
            char_return = lower_alphabet[rotated_index]
        else:
            char_return = lower_alphabet[rotated_index % 26]
    return char_return

def encrypt(text, rot):
    encrypt = ''

    for i in text:
        encrypt += rotate_character(i, rot)
    return encrypt
