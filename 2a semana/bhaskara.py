import math			# habilita cálculos match.

# inputs de dados
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


# fórmulas báiscas de uma equação quadrática

delta = (b ** 2) - (4 * a * c)


# condicionais e ordenação
if delta == 0:			# uma única raíz
	raiz1 = -b + math.sqrt(delta) / (2 * a)
	print("a raíz desta equação é ", raiz1)
else:
	if delta < 0:
		print("esta equação não possui raízes reais")
	else:
		raiz1 = -b + math.sqrt(delta) / (2 * a)
		raiz2 = -b - math.sqrt(delta) / (2 * a)
		if raiz1 <= raiz2:
			print("as raízes da equação são", raiz1, "e", raiz2)
		else:
			print("as raízes da equação são", raiz2, "e", raiz1)