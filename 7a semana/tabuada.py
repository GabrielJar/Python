linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end = "\t")
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1




def tabuada():
    # parte faltante
    tab = 1
    while tab <= 10:
        i = 1
        while i <= 10:
            print(tab,"x",i,"=",tab*i)
            i = i + 1
        print()
        tab = tab + 1
tabuada()


altura = 5
linha = 1
while linha <= altura:
    print("*", end = "")
    coluna = 2
    while coluna < altura: 
        if linha == 1 or linha == altura:
            print("*", end = "")
        else:
            print(end = " ")
        coluna = coluna + 1
    print("*")
    linha = linha + 1
