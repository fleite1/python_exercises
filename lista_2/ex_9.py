'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.'''

even_numbers_list = []
odd_numbers_list = []

while True:
    number = int(input('Enter a number (0 to exit): '))
    
    if number == 0:
        print(f'Even numbers entered: {even_numbers_list}')
        print(f'Quantity of even numbers: {len(even_numbers_list)}')
        print('-----------------')
        print(f'Odd numbers entered: {odd_numbers_list}')
        print(f'Quantity of odd numbers: {len(odd_numbers_list)}')
        break
    
    if number < 0:
        print('Negative number. Please enter a positive number.')
    elif number % 2 == 0:
        even_numbers_list.append(number)
    else:
        odd_numbers_list.append(number)
