'''Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""

#''O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
#Caso contrário,ele será classificado como""Inocente"".""'''

cont = 0

print('Press y to yes and n to no')

question_1 = input('Did you call the victim? ')
if question_1 == 'y': 
    cont += 1

question_2 = input('Have you been at the location of the crime? ')
if question_2 == 'y' :
    cont += 1

question_3 = input('Do you live close to the victim? ')
if question_3 == 'y':
    cont += 1

question_4 = input('Do you owe any money to the victim? ')
if question_4 == "y":
    cont += 1


question_5 = input('Did you work with the victim? ')
if question_5 == "y":
    cont += 1

if cont >= 5:
    print('Murderer')

elif cont <= 4 and cont >= 3:
    print("accomplice")
    
    
elif cont == 2:
    print('Suspect')
    
else: 
    print('innocent')