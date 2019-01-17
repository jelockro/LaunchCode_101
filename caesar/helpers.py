import string
alphalist = [x for x in string.ascii_lowercase]


def alphabet_position(letter):
    lower_letter = letter.lower()
#    print(type(alphalist.index(lower_letter)))
    return alphalist.index(lower_letter)


def rotate_character(char, rot):
    if char.isalpha():
        newPos = (alphabet_position(char) + (rot % 26)) % 26
        if char.isupper():
            return alphalist[newPos].upper()
        else:
            return alphalist[newPos]
    else:
        return char
