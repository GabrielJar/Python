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

def n_primos(limite):
    n = 2
    contador = 0
    # Loop de testes respostas
    while n < limite:
        if éPrimo(n):
            print(n, end = " ")
            contador = contador + 1
            n = n + 1
        else:
            n = n + 1
    print() # Quebra de linha
    print("Foram encontrados: " + str(contador) + " números primos")
    return contador


#----------------------------------------------------------------------- Início

# Entrada de dados
limite = int(input("Digite um número inteiro: "))
if limite < 2:
    print("Digite um número maior que 1")
    limite = int(input("Digite um número inteiro: "))
n_primos(limite)
