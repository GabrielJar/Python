'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 2, 4, 43, 5, 676, 45, 76, 768, 34, 768, 676, 43]
print("Lista completa/original: " + str(lista))
print()
'''

def remove_repetidos(lista):
    nova_lista = [] # Onde colocar os itens unicos
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
            # print(nova_lista)
    # print()
    # print("Nova lista de números únicos: " + str(nova_lista))
    nova_lista.sort()
    # print("Nova lista ordenada: " + str(nova_lista))
    return nova_lista

'''
lista = remove_repetidos(lista)
print()
print("Lista final = " + str(lista))
'''
