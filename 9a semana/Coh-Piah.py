'''
Tamanho médio da palavra



'''


def tamanho_medio_palavra(texto):
    media = 0
    palavras = 0
    tamanho_total = 0
    for palavra in texto:
        palavras = palavras + 1
        tamanho = len(palavra)
        tamanho_total = tamanho_total + tamanho
        media = tamanho_total / palavras
