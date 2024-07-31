'''Faça um Programa que peça dois números e imprima o maior deles.'''
num_1 = float(input('Digit the first number:'))
num_2 = float(input('Digit the second number:'))

if num_1 > num_2:
    print(f"The biggest number is {num_1}")

elif num_1 < num_2:
    print(f"The biggest number is {num_2}")
    
else:
    print("Both numbers are equal.")
