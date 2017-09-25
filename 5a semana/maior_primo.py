def éPrimo(k):
	fator = 2
	if k == 2:
		return True
	while (k % fator) != 0 and fator <= (k / 2):
                fator = fator + 1
	if k % fator == 0:
		return False					
	else:
		return True			

def maior_primo(x):
	contador = 2
	primo_anterior = 2
	while contador <= x:
		if éPrimo(contador):			
			primo_anterior = contador	
			contador = contador + 1
		else:
			contador = contador + 1
	return primo_anterior
