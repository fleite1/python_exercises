'''Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.
'''
num_1 = float(input('Enter the first number: '))
num_2 = float(input('Enter the second number: '))
num_3 = float(input('Enter the third number: '))

if num_1 > num_2 and num_1 > num_3:
    print(f'The number {num_1} is the biggest')

elif num_2 > num_3 and num_2 > num_1:
    print(f'The number {num_2} is the biggest')
    
else:
     print(f'The number {num_3} is the biggest')