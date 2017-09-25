# Função que determina partida simples ou campeonato  ===> TALVEZ TENHA QUE EMBUTIR NA FUNCAO PRINCIPAL
def escolha():

    # Escolha do tipo de jogo (partida simples ou campeonato)
    print("1 - para jogar uma partida isolada")
    partidas = int(input("2 - para jogar um campeonato "))

    # Verificação de opções e validade da resposta
    while partidas < 1 or partidas > 2:
        partidas = int(input("Selecione novamente apenas 1 ou 2 "))

    if partidas == 1:
        numero_partidas = 1
        print("Você escolheu uma partida!")
    elif partidas == 2:
        numero_partidas = 3
        print("Voce escolheu um campeonato!")

    # Início do campeonato
    campeonato(numero_partidas)


# Função da jogada do jogador (input manual)
def usuario_escolhe_jogada(n, m):
    jogada = 0

    # Loop de verificação até acertar
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))

        # Ao inserir valor inválido repete
        if jogada > m or jogada > n or jogada < 1:
            print("Oops! Jogada inválida! Tente de novo.")
            jogada = 0  # Volta o status para 0 e repete o loop

        # Valor válido retorna quantidade de peças
        else:
            return jogada


# Função da jogada do computador
def computador_escolhe_jogada(n, m):

    # Se houver menos peças que o máximo, retirar todas as peças
    if n <= m:
        return n
    else:

        # Verifica possibilidade de múltiplos de (m + 1)
        jogada = n % (m + 1)

        # Retira um conjunto múltiplo de (m + 1)
        if jogada > 0:
            return jogada
        # Retira o máximo de peças
        else:
            return m


# Função da partida
def partida():
    
    # Entrada das informações pelo usuário
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # Validação da entrada de limite de peças
    if m == 0 or m > n:
        while m <= 0:
            print("Oops! Valor inválido! Tente outro valor.")
            jogada = int(input("Limite de peças por jogada? "))

    # Variável da vez do computador
    vez_computador = True

    # Verificação de quem começa
    if n % (m + 1) == 0:
        vez_computador = False  # Mudança de status para convidar jogador primeiro
        print("Voce começa!")
    else:
        print("Computador começa!")

    # Início dos loops de jogada
    while n > 0:
        if vez_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_computador = False
            print("O computador tirou " + str(jogada) + " peças")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_computador = True
            print("Você tirou " + str(jogada) + " peças")

        # Retirada de peças
        n = n - jogada

        # Exibe quantas peças estão no jogo
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam apenas " + str(n) + " peças no tabuleiro.")
            
    # Quem venceu com base na última jogada / mudança de status
    if vez_computador:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0
    
# Função que controla a quantidade de partidas no campeonado ===> PEDE PARA CHAMAR PARTIDA TRES VEZES DENTRO
def campeonato(x):
    
    # Contador de rodadas
    rodada = 1

    # Variáveis de vitórias
    vitorias_usuario = 0
    vitorias_computador = 0

    # Loop de jogos até o limite escolhido pelo usuário
    while rodada <= x:

        # imprime rodada e chama uma partida
        print("**** Rodada " + str(rodada) + " ****")
        partida()

        # Conta resultados
        # Vitória do usuário
        if partida == 1:
            vitorias_usuario += 1

        # Vitória do computador
        else:
            vitorias_computador += 1

        # Aumenta contagem para próxima rodada
        rodada += 1

    # Saída do loop e final do campeonato. Imprime resultados
    print("**** Final do campeonato! ****")
    print("Placar: Você " + str(vitorias_usuario) + " X " + str(vitorias_computador) + " Computador")


### Início do Jogo ###

# Mensagem de boas vindas
print("Bem-vindo ao jogo do NIM! Escolha:")
escolha()
