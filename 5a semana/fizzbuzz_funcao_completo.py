x = int(input("Digite um número: "))

def fizzbuzz(x):
	if (x % 3 == 0) and (x % 5 != 0):
		print("Fizz")
	elif (x % 5 == 0) and (x % 3 != 0):
		print("Buzz")
	elif (x % 3 == 0) and (x % 5 == 0):
		print("FizzBuzz")
	else:
		return x
		print(x)
		
fizzbuzz(x)