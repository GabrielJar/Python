print("Digite um número para ver seu fatorial ou um negativo para sair.")
n = int(input("Digite um número inteiro positivo: "))

def fatorial(x):
    fatorial = 1
    while x > 1:
        fatorial = fatorial * x
        x = x - 1
    return fatorial

# repetição com validação de saída
while n >= 0:
    print(fatorial(n))

    # Saída
    n = int(input("Digite um número inteiro positivo: "))
 
# mensagem de saída
print("Tchau tchau! ;)")
