def is_prime(x):
    if x < 2:
        return False
    else:
        if x == 2:
            return True
        else:
            n = 2
            primo = True
            while n < (x - 1) and primo == True:
                if x % n != 0:
                    n = n + 1
                else:
                    n = n + 1
                    primo = False
            return primo

entrada = int(input("Digite um número: "))

if is_prime(entrada):
    print(str(entrada) + " é primo!")
else:
    print(str(entrada) + " não é primo!")
