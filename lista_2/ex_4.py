'''Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.'''

grade = float(input('Digit your grade: '))
if grade >= 7 and grade<= 10:
    print(f"Your grade is {grade}, so you are approved")
    
elif grade < 7 and grade >=0:
    print(f"Your grade is {grade}, so you didn't pass")

else:
    print('The grade has to be between 0 to 10')

