num = input("Digite um número inteiro: ")

rest = int(num) % 100     # Ao dividir por 100, pega a diferença da divisão que é a quantidade de dezenas.
result = rest // 10       # AO dividir a quantidade do resto por 10, você mostra a quantidade de dezenas inteiras.

print ("O dígito das dezenas é", result)

""""
Para resolver, lembrar que:
O primeiro dígito de um número é a unidade, o segundo a dezena e o terceiro a centena
Para achar a centeza basta dividir por 10 e para achar a dezena basta dividir um número por 100, se não tiver suficiente, não há centenas e dezenas em um número.
"""