numero = int(input("Digite um número inteiro: "))

if numero == 0 or numero == 1 or numero == 2:
	print("Primo!")
else:	
	if (numero % 2) != 0:
		primo = True
		primo_anterior = numero
		print(str(numero) + " É primo!")
	else:
		print(str(numero) + " NÃO é primo")
			break
print("valor de i foi: " + str(i))