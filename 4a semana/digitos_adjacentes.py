numero = int(input("Digite um número: "))   ### Entrada do número a ser comparado


### Definições de entradas para o while/repetição funcionar

adjacenteIgual = False                          ### Pré definição do boolean para falso/não
unidadeAnterior = numero % 10                   ### Definição da primeira unidade para comparação
numero = numero // 10                           ### Redução do número para próxima comparação de unidade


### Entrada da repetição/while

while numero > 0 and not adjacenteIgual:        ### Verificações de entrada do while/repetição
    unidadeAtual = numero % 10                  ### Definição da unidade atual para comparação
    numero = numero // 10                       ### Redução do número para próxima repetição ou saída da repetição
    if unidadeAtual == unidadeAnterior:         ### Comparação
        adjacenteIgual = True
    unidadeAnterior = unidadeAtual              ### Definição da unidade anterior para comparação na próxima repetição 


### Saída da repetição para impressão do resultado

if adjacenteIgual:
    print("sim")
else:
    print("não")
