'''Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.'''

age = int(input('Enter your age: '))

if age <= 12:
    print(f"You have {age} years old, so you are a child")

elif age >=13:
    print(f'You have {age} years old, so you are a teen')
    
elif age >= 20:
     print(f'You have {age} years old, so you are a adult')
     
else:
     print(f'You have {age} years old, so you are a elderly')