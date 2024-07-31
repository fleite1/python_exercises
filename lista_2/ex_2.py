'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

day_period = input('Digit the time of the day, M for morning, A for Afternoon and N for Night:  ')

if day_period == 'M':
    print("Good Morning!")

elif day_period == 'A':
    print("Good Afternoon!")
    
elif day_period == 'N':
    print("Good Night!")

else: 
    print("Invalid input. Please enter M, A, or N.")