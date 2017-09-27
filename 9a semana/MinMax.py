def MinMax(temperaturas):
    print("A menor temperatura do mês foi: " + minima(temperatura), "C.")
    print("A maior temperatura do mês foi: " + maxima(temperatura), "C.")

def minima(temps):
    min = temps[0]
    i = 1 # Contador
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def maxima(temps):
    max = temps[0]
    i = 1 # Contador
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def teste_pontual_minima(temp, valor_esperado):
    valor_calculado = minima(temp)
    mensagem_erro(temp, valor_esperado, valor_calculado)

def teste_pontual_maxima(temp, valor_esperado):
    valor_calculado = maxima(temp)
    mensagem_erro(temp, valor_esperado, valor_calculado)

def mensagem_erro(temp, valor_esperado, valor_calculado):
    if valor_calculado != valor_esperado:
        print("Valor errado para array: ", temp)
        print("Valor esperado era: ", valor_esperado, ". Valor calculado: ", valor_calculado)



# ------------------------TESTES AUTOMATIZADOS

def teste_completo():
    testa_minima()
    testa_maxima()

def testa_minima():
    print("Iniciando testes de mínimas")
    teste_pontual_minima([0], 0)
    teste_pontual_minima([0, 0, 0, 0, 0, 0], 0)
    teste_pontual_minima([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual_minima([30, 27, 25, 26, 29, 31, 32, 33, 30, 29, 24, 22, 26, 30, 27, 24, 25, 26, 24], 22)
    teste_pontual_minima([-15, -12, 0, 20, 30], -15)
    print("Finalizando testes de mínimas")
    print()

def testa_maxima():
    print("Iniciando testes de máximas")
    teste_pontual_maxima([0], 0)
    teste_pontual_maxima([0, 0, 0, 0, 0, 0], 0)
    teste_pontual_maxima([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    teste_pontual_maxima([30, 27, 25, 26, 29, 31, 32, 33, 30, 29, 24, 22, 26, 30, 27, 24, 25, 26, 24], 33)
    teste_pontual_maxima([-15, -12, 0, 20, 30], 30)
    print("Finalizando testes de máximas")
    print()


#-------------------------COMANDOS

teste_completo()
