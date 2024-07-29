'''Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.'''

fuel_consumed = float(input('Enter the amount of liters consumed: '))
distance = float(input('Enter the distance traveled: '))

if distance == 0:
        print("Distance traveled cannot be zero.")
else:
        average_consumption = fuel_consumed / distance
        print(f"The average fuel consumption is {average_consumption:.2f} liters per kilometer.")