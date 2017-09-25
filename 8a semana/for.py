frutas_exoticas = ["jabuticaba", "cupuaçu", "graviola"]

for fruta in frutas_exoticas:
    print("Eu adoro " + fruta)


#----------------------------------------------------------------

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print()
print(primos)
print(len(primos))

for x in primos:
    print("O quadrado de " + str(x) + " é " + str(x * x))


#----------------------------------------------------------------
'''
for i in range(20): #Percorre ao limite, e vai de zero ao limite
    # fazer algo

for i in range(3, 20): #Percorre do inicial ao limite
    # fazer algo

for i in range(3, 20, 2): # Percorre do inicial ao limite seguindo o passo / 3o item
    # fazer algo
'''

print()
print("Imprimir o for no range de 10 a 20: ")
for i in range(10, 20):
    print(i, end = " ")

print()
print()
print("Imprimir o for no range de 0 a 40 com passo 2: ")
for i in range(0, 40, 2):
    print(i, end = " ")

print()
print()
print("Imprimir o for no range de 100 a 0 com passo -5: ")
for i in range(100, 0, -5):
    print(i, end = " ")

print()
print()
print(primos)
for i in range(len(primos)):
    primos[i] = primos[i]**3
print(primos)
