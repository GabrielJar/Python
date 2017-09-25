def vogal(c):
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        return True
    else:
        return False

letra = str(input("Digite uma letra: "))

if vogal(letra):
    print(letra + " é Vogal - True")
else:
    print(letra + " é Consoante - False")
