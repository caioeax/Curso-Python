""" Calculadora com While """

## Eu fiz assim:

# while True:
#     numero_1 = int(input('Digite um número: '))
#     numero_2 = int(input('Digite outro número: '))
#     operador = input('Digite o operador: ')

#     print(operador == '*')
#     print(operador == 'x')

#     if operador == '*' or operador == 'x':
#         print(f'o resultado é: {numero_1 * numero_2}')
#     elif operador == '/':
#         print(f'o resultado é: {numero_1 // numero_2}')
#     elif operador == '+':
#         print(f'o resultado é: {numero_1 + numero_2}')
#     elif operador == '-':
#         print(f'o resultado é: {numero_1 - numero_2}')

#     ########
#     sair = input('Quer sair? [s]im: ').lower().startswith('s')

#     if sair is True:
#         break

while True:
    numero_1_str = input('Digite um número: ')
    numero_2_str = input('Digite outro número: ')
    operador = input('Digite o operador: ')

    numeroValido = None
    numero_1 = 0 
    numero_2 = 0 

    try:
        numero_1 = float(numero_1_str) 
        numero_2 = float(numero_2_str) 
        numeroValido = True
    except:
        numeroValido = None

    if numeroValido is None:
        print('Erro! Número incorreto.')
        continue

    operadoresPermitidos = 'x*/+-'

    if len(operador) != 1:
        print('Apenas um operador!')
        continue

    if operador not in operadoresPermitidos:
        print('Erro! Operador lógico não disponível ou incorreto!')
        continue

    if operador == '*' or operador == 'x':
        print(f'o resultado é: {numero_1} * {numero_2} = {numero_1 * numero_2}')
    elif operador == '/':
        print(f'o resultado é: {numero_1} / {numero_2} = {numero_1 // numero_2}')
    elif operador == '+':
        print(f'o resultado é: {numero_1} + {numero_2} = {numero_1 + numero_2}')
    elif operador == '-':
        print(f'o resultado é: {numero_1} - {numero_2} = {numero_1 - numero_2}')

    ########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break