'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 2, 4, 43, 5, 676, 45, 76, 768, 34, 768, 676, 43]
print("Lista completa/original: " + str(lista))
print()
'''

def soma_elementos(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

'''
print()
print("Lista final = " + str(soma_elementos(lista)))
'''
