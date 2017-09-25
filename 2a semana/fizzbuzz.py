number = int(input("Insira um n?mero: "))

validation1 = number % 3
validation2 = number % 5

if(validation1 == 0) and (validation2 == 0):
	print("FizzBuzz")
else:
	print(number)