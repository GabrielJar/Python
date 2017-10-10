def censor(text, word):
  
  #------------------------ VALIDAES
  print("Texto de entrada: " + str(text))
  print("Palavra de entrada: " + str(word))
  #--------------------------------- 
  
  block = "*" * len(word) 
  text_list = text.split()
  new_text = []
  
  #------------------------ VALIDAES
  print("Bloqueio: " + str(block) + " = " + str(len(word)) + " letras da palavra '" + str(word) + "'")
  print("Lista de entrada: " + str(text_list))
  #---------------------------------
  
  for palavra in text_list:
    if palavra == word:
  		new_text.append(block)
    else:
      new_text.append(palavra)
  print(" ".join(new_text))
  return " ".join(new_text)


'''
Opção B editando apenas a lista original

def censor2(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
'''
