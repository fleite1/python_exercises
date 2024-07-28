'''Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão'''

num_1 = int(input('Digit number 1 number: '))
num_2 = int(input('Digit number 2 number: '))

add = num_1 + num_2
sub = num_1 - num_2
mult = num_1 * num_2



print(f"The addition of {num_1} + {num_2} is {add}")
print(f"The subtraction of {num_1} - {num_2} is {sub}")
print(f"The multiplication of {num_1} x {num_2} is {mult}")

if num_2 == 0:
    print("Error division by 0")
else:
    div = num_1 / num_2
    print(f"The division of {num_1} / {num_2} is {div}")

