linha_maxima = int(input("Insira a largura do retângulo: "))
coluna_maxima = int(input("Insira a altura do retângulo: "))

linha = 1
coluna = 1

while coluna <= coluna_maxima:    
    while linha <= linha_maxima:
        if linha == 1 or linha == linha_maxima:
            print("#", end = "")
        else:
            if coluna == 1 or coluna == coluna_maxima:
                print("#", end = "")
            else:
                print(" ", end = "")
        linha = linha + 1
    coluna = coluna + 1
    print()
    linha = 1
