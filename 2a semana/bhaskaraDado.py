import math

a = float(input("Digite o valor da A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b ** 2) - (4 * a * c)

if delta == 0:
	raiz1 = (-b + math.sqrt(delta)) / (2 * a)
	print("A ?nica raiz ?: ", raiz1)
else:
	if delta < 0:
		print("Esta equa??o n?o possui ra?zes reais")
	else:
		raiz1 = (-b + math.sqrt(delta)) / (2 * a)
		raiz2 = (-b - math.sqrt(delta)) / (2 * a)
		print("A primeira raiz ?: ", raiz1)
		print("A segunda raiz ?: ", raiz2)