'''Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.'''

side1 = int(input('Enter the side of the triangle 1: '))
side2 = int(input('Enter the side of the triangle 2: '))
side3 = int(input('Enter the side of the triangle 3: '))

if side1 == side2 and side1 == side3:
    print('The triangle is equilateral')
    
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('The triangle is isosceles')
    
else :
    print('The triangle is scalene')