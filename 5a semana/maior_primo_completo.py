n = int(input("Digite um número inteiro maior que 2: "))
contador = 0

# Teste de número de entrada maior ou igual que dois
if n <= 2:
        n = int(input("Digite um número inteiro maior que 2: "))


# Função que define primos
def éPrimo(x):
	fator = 2
	
	# Definição do 2 como primo
	if x == 2:
		return True
		
	# Definições do loop e da saída, apenas testar até a metade do limite (n)
	while (x % fator) != 0 and fator <= (x / 2):
		fator = fator + 1
		
	if x % fator == 0:
		return False					# Status de não primo (não está sendo utilizaado) 
	else:
		return True						# Status de Primo

		
# Função que testa todos os números até o número limite (n)
def maior_primo(x):
	contador = 2						# Início a partir do 2
	primo_anterior = 2					# Definição de um primo máximo anterior/incial
	
	# Definições do loop e da saída
	while x <= n and contador <= n:
		if éPrimo(contador):			# Validação de "primalidade"
			primo_anterior = contador	# Guarda primo encontrado
			contador = contador + 1
		else:
			contador = contador + 1
	return primo_anterior				# Saída devolve o último primo encontrado

# Roda as funções e devolve a resposta
print("O maior número primo anterior de " + str(n) + " é: " + str(maior_primo(n)))
