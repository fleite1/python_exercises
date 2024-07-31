'''Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.'''

question_1 = input('What is your name? ')
question_2 = int(input('How old are you? '))
question_3 = input("What you do in college? ")
question_4 = input("Which soccer team do you support? ")

my_age = 23
my_team = 'Avaí'

if question_2 > my_age:
    age_comparison = "You are older than me."
elif question_2 < my_age:
    age_comparison = "You are younger than me."
else:
    age_comparison = "You are the same age as me."

if question_4.lower() == my_team.lower():
    team_comparison = "It's great that we support the same team!"
else:
    team_comparison = "We don't support the same team."

print(f'Hello {question_1}, nice to meet you! I am {my_age} years old. {age_comparison} Nice that you are studying {question_3} in college. {team_comparison}')
