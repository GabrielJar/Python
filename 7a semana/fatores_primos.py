# Função para saber se é primo
def éPrimo(x):

    # Variável para divisão/módulo
    fator = 2

    # Definição de 2 como primo hard coded
    if x == 2:
        return True

    # Loop para encontrar um divisor
    while x % fator != 0 and fator <= (x / 2):
        fator = fator + 1

    # Se encontrou divisor, não é primo
    if x % fator == 0:
        return False
    # Se não encontrou, é primo!
    else:
        return True


### Início

# Entrada de dados
n = int(input("Digite um número inteiro: "))

# Loop de testes respostas
while n > 0:
    if éPrimo(n):
        print(n, " é primo!")
    else:
        print(n, " não é primo. :-(")
    n = int(input("Digite um número inteiro: "))
