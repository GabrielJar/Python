number = int(input("Insira um n?mero: "))

validation = number % 5

if(validation == 0):
	print("Buzz")
else:
	print(number)