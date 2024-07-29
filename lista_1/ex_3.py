'''Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.'''

distance= int(input('Enter the distance in KM: '))

meters = distance * 1000
centimeters = distance * 100000
millimeters = distance * 1000000

print(f"The distance in kilometers is {distance}, in meters is {meters}, in centimeters is {centimeters}, and in millimeters is {millimeters}")