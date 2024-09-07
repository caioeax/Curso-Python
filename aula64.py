"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# while True:
#     trueCpf = ''
#     tamanhoCpf = 0
#     i = 0
#     valorMulti = 0
#     index_2 = 10
#     cpfInput = input('CPF: ')   
#     tamanhoCpf = len(cpfInput)
#     print()

#     if tamanhoCpf > 14 or tamanhoCpf < 14:
#         print('Erro! CPF incorreto.')

#     trueCpf = f'{cpfInput[:3]}{cpfInput[4:7]}{cpfInput[8:11]}{cpfInput[12:]}'

#     while i < tamanhoCpf - 5:
#         valorMulti = valorMulti + int(trueCpf[i]) * index_2
#         i += 1
#         index_2 -= 1

#     valorMultiFinal_1 = valorMulti * 10
#     verifyCpf = valorMultiFinal_1 % 11

#     if verifyCpf == 10:
#         verifyCpf = 0
    
#     if verifyCpf == int(trueCpf[9]):
#         print(f'CPF válido! Seu CPF é: {cpfInput}')
#         break
#     else:
#         print('CPF incorreto!')
#         continue

import re

import random

for _ in range(100):
    trueCpf = ''
    cpfInput = ''
    tamanhoCpf = 0
    i = 0
    j = 0
    index_2 = 0
    valorMulti = 0
    cpfInput = input('CPF: ')  
    print()

    trueCpf = cpfInput.replace(".","").replace("-","") 
    # trueCpf = re.sub(r'[^0-9]', '', cpfInput)
    tamanhoCpf = len(trueCpf)

    if tamanhoCpf > 11 or tamanhoCpf < 11:
        print('Erro! CPF incorreto.')
        break

    index_2 = 10

    while i < tamanhoCpf - 2:
        valorMulti = valorMulti + int(trueCpf[i]) * index_2
        i += 1
        index_2 -= 1

    valorMultiFinal_1 = valorMulti * 10
    verifyCpf = valorMultiFinal_1 % 11

    if verifyCpf == 10:
        verifyCpf = 0
    
    if verifyCpf == int(trueCpf[9]):
        index_2 = 11
        valorMulti = 0

        while j < tamanhoCpf - 1:
            valorMulti = valorMulti + int(trueCpf[j]) * index_2
            j += 1
            index_2 -= 1

        valorMultiFinal_2 = valorMulti * 10
        verifyCpf2 = valorMultiFinal_2 % 11

        if verifyCpf2 == 10:
            verifyCpf2 = 0
        if verifyCpf2 == int(trueCpf[10]):
            print(f'Cpf válido. CPF: {cpfInput}')
            break
        else:
            print(cpfInput)
            print('CPF digitado incorretamente!')
            continue
    else:
        print(cpfInput)
        print('CPF digitado incorretamente!')
        continue