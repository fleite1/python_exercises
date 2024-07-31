'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.'''

salary = float(input('What is your hourly salary?  '))
hours_work = float(input('How many hours do you work per month?  '))

salary_month = salary * hours_work

print(f"Your salary per month is {salary_month:.2f}!")


