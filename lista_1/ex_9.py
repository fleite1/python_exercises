'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.'''

workout_hours = float(input('How many hours do you workout per week? '))
calories_per_hour = 5
calories_burned = (calories_per_hour * workout_hours) * 4
print(f"You burn approximately {calories_burned:.2f} calories per month")