from helpers import rotate_character


def encrypt(text, rot):
    encode_text = ''
    for c in text:
        encode_text += rotate_character(c, rot)
    return encode_text


def main():
    from sys import argv
    text = input("Type a message: ")
    try:
#       print('arv[1]', type(argv[1]))
        encrypt(text, int(argv[1]))
    except (IndexError, ValueError):
        rotation = int(input("\nRotate by: "))
        encrypt(text, rotation)


if __name__ == "__main__":
    main()
