lista = []
contador = -1
entrada = int(input("Digite um número para adicionar a lista e '0' para imprimir: "))

while entrada != 0:
    lista.append(entrada)
    entrada = int(input("Digite um número inteiro: "))

#print("A quantidade de intens na lista é de: " + str(len(lista)))
#print("A lista contém: " + str(lista))

quantidade = len(lista)

while quantidade > 0:
    print(lista[contador])
    quantidade = quantidade - 1
    contador = contador - 1
