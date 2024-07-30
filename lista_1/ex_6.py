'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

dist = float(input("What distance will you travel(in kilometers)?: "))
 
speed_by_airplane = 600
speed_by_car = 100
speed_by_bus = 80

time_by_airplane = dist/speed_by_airplane
time_by_car = dist/speed_by_car
time_by_bus = dist/speed_by_bus

print(f'The travel time by airplane is {time_by_airplane:.2f} hour(s), by car is {time_by_car:.2g} hour(s) and by bus is {time_by_bus:.2f} hour(s)')

