'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

salary = float(input("Enter your gross salary: "))


if salary < 1903.98:
    print(f"You don`t need to pay taxs, your salary is {salary:.2f}.")

elif salary <= 2826.65:
    tax = (salary * 7.5)/100
    net_salary = salary - tax
    print(f'Your salary with taxes is {net_salary:.2f}')
    
elif salary <= 3751.05:
    tax= (salary * 15)/100
    net_salary = salary - tax
    print(f'Your salary with taxes is {net_salary:.2f}')
    
elif salary <= 4664.68:
    tax = (salary * 22.5)/100
    net_salary = salary - tax
    print(f'Your salary with taxes is {net_salary:.2f}')
    
else:
    tax = (salary * 27.5)/100
    net_salary = salary - tax
    print(f'Your salary with taxes is {net_salary:.2f}')
    