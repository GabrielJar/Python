numero = int(input("Digite o valor de n: "))

contador = 1
fatorial = 1

while contador <= numero and contador != 0:
	fatorial = fatorial * contador
	contador = contador + 1

print(fatorial)
