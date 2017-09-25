entrada_largura = int(input("Insira a largura do trângulo: "))
altura = int(input("Insira a altura do triângulo: "))

while altura > 0:
    largura = entrada_largura
    while largura > 0:
        print("#", end = "")
        largura = largura - 1
    altura = altura - 1
    print()
    
