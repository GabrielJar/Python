lista1 = ["vermelho", "verde", "azul"]
print("Lista1 = " + str(lista1))

lista2 = lista1
print("Lista2 clone de lista1 = " + str(lista2))

lista2[0] = "rosa"
print("Adicionamos rosa na posição 0 em lista2")
print("Lista1 = " + str(lista1))
print("Lista2 clone de lista1 = " + str(lista2))

print()


#-------------------------------------------------

lista1 = ["vermelho", "verde", "azul"]
lista2 = lista1[:]
print("Lista1 = " + str(lista1))
print("Lista2 criada com clone lista1[:] = " + str(lista1))
lista2[0] = "rosa"
print("Adicionamos rosa na posição 0 em lista2")
print("Lista1 = " + str(lista1))
print("Lista2 clone de lista1 = " + str(lista2))

print("Rosa está na lista1?")
if "rosa" in lista1:
    print("Está!")

print("Vermelho está na lista1?")
if "vermelho" in lista1:
    print("Está")
else:
    print("Faltou")

print([1, 2] + [3, 4])

a = [1, 2, 3]
b = [4, 5, 6]
print("lista a: " + str(a))
print("lista b: " + str(b))

print("lista concatenada de (a + b): " + str(a + b))
print("lista concatenada de (a + b + a): " + str(a + b + a))


print("Lista a: " + str(a))
a.append("gato")
print("Com append: " + str(a))

b_quintuplicado = b * 5
print("lista b quintuplicada (b * 5): " + str(b_quintuplicado))
print("Quantidade de intens na lista quintuplicada: " + str(len(b_quintuplicado)))

lista = ['a', 'b', 'c', 'd', 'e', 'f']
print(lista)
del lista[1:5]
print("Lista retirada uma parte com 'del lista[1:5]': " + str(lista))
