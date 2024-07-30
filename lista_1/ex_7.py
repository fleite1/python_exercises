'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''

weight = float(input("Enter your weight in kilograms:  "))
height = float(input('Enter your height in meters: '))

IMC = weight / (height * height) 

print(f"Your IMC is {IMC:.2f}")

