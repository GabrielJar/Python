tamanho = int(input("Digite o tamanho da sequência de números: ")) #definição do limite
produto = 1 #valor neutro para não travar o while
i = 0 #vaor neutro/inicial

while i < tamanho:
	valor = int(input("Digite um valor a ser multiplicado: "))
	produto = produto * valor
	i = i + 1
	
print("O produto dos valores digitados é ", produto)