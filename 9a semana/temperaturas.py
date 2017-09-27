qual a temperatura maxima?
qual a temperatura minima?

def MinMax(temperaturas):
    print("A menor temperatura do mês foi: " + minima(temperatura), "C.")
    print("A maior temperatura do mês foi: " + maxima(temperatura), "C.")

    
def minima(temps):
    min = 0
    i = 0 # Contador
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
        
