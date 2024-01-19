def abc(string):
    if string in ["A", "a"]: # Basis tilfellet: "A", "a" 
        return string
    else:
        number = ord(string) - 1
        character = chr(number)

        return abc(character) + string


def main():
    letter = input("Please enter a letter: ")
    print(abc(letter))


if __name__ == '__main__':
    main()
