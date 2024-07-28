'''Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.'''

year = int(input("What year were you born? : "))
actual_year = int(input('What year are we? : '))

age = actual_year - year 

print(f'You have {age} year(s) old')

if age <= 12:
    print("You are a child")
    
elif age >= 13 and age <= 19:
    print("You are a teen")
    
elif age >= 20 and age<=59:
    print('You are an adult')
    
elif age >= 60:
    print('You are Elderly')