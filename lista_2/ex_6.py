'''Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.'''

login = input('Enter your login: ')
password = input('Enter your password: ')

if login == 'admin' and password == 'admin123' :
    print('You can pass')
    
else:
    print('EError: Invalid login or password')