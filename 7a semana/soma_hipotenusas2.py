def é_hipotenusa(a, b):
    return ((a ** 2) + (b ** 2))
 
def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        c2 = (c ** 2)      
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (c2 == é_hipotenusa(a, b)):
                    print(a, " - " ,b , " - " , c)
                    soma = soma + c
                    a = n
                b = b + 1
            a = a + 1
            b = a
        c = c + 1
    return soma


### Início

n = int(input("Digite um número inteiro: "))
if n <= 0:
    print("Digite um número positivo")
    n = int(input("Digite um número inteiro: "))

print(str(soma_hipotenusas(n)))
