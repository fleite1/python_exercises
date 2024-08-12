'''Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.'''


averages = []

for i in range(1, 6):
    print(f'Student {i}')
    grades = []
    
    for x in range(1, 6):
        grade = float(input(f'Enter grade {x}: '))
        grades.append(grade)
    
    average = sum(grades) / len(grades)
    averages.append(average)

passed_students = sum(1 for average in averages if average >= 7.0)

print(f'Number of students with an average grade greater than or equal to 7.0: {passed_students}')
