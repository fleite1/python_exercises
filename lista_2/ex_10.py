'''Faça um programa que lê três números inteiros e os mostra em ordem
crescente.'''

num_1 = int(input('Digit the first number: '))
num_2 = int(input('Digit the second number: '))
num_3 = int(input('Digit the third number: '))

if num_1 > num_2 and num_2 > num_3:
    print({num_1}, {num_2}, {num_3})
    
elif num_1 > num_3 and num_3 > num_2:
    print({num_1}, {num_3}, {num_2})    
      
elif num_2 > num_1 and num_1 > num_3:
    print({num_2}, {num_1}, {num_3})
    
elif num_2 > num_3 and num_3 > num_1:
    print({num_2}, {num_3}, {num_1})
    
elif num_3 > num_2 and num_2 > num_1:
    print({num_3}, {num_2}, {num_1})
    
elif num_3 > num_1 and num_1 > num_2:
    print({num_3}, {num_1}, {num_2})
    
    
