text = "abc"

def reverse(text):
  lista_letras = []
  lista_letras_inversa = []
  x = -1
  for letra in text:
    lista_letras.append(letra)
    # Validar input de letras
    print (letra)


  quantidade = len(lista_letras)
  
  # Validar quantidade de letras e lista em si 
  print("Lista: " + str(lista_letras))
  print("Quantidade : " + str(quantidade))
  
  contador = -1
  
  while contador < quantidade:
    lista_letras_inversa.append(lista_letras[-1])
    lista_letras = lista_letras[0,len(lista_letras) - 1]
  
  quantidade2 = len(lista_letras_inversa)
    
  # Validar quantidade de letras e lista em si 
  print("Lista: " + str(lista_letras_inversa))
  print("Quantidade : " + str(quantidade2))
  

reverse(text)

  # Transformar a string em uma lista
  # Fazer for item a item negativo
  # Inserir os dados da lista em ordem reversa em nova lista
