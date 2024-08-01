'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.'''

grade = float(input("Digit your grade between 0 to 10: "))
if grade <= 0 and grade <= 10:
    print(f'Your grade is {grade}')
    
else:
    print(f"Invalide grade {grade}, the grade has to be between 0 to 10")
    
    
