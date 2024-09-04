"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# number = input('Digite um número! ')
# numberInt = float(number)

# if number.isdigit():
#     if numberInt % 2 == 0:
#         print('Seu número é par!')
#     else:
#         print('Seu número é ímpar!')
# else:
#     print('Seu número não é inteiro!')

# hour = input('Qual o horário atual? (HH:MM)')

# hourInt = int(hour[0:2])
# minutesInt = int(hour[3:5])

# if hourInt < 0 or hourInt > 23 or minutesInt < 0 or minutesInt > 59:
#     print('Horário errado!')
# elif hourInt < 12:
#     print('Bom dia!')
# elif hourInt < 17:
#     print('Boa Tarde!')
# else:
#     print('Boa noite!')

name = input('Qual seu primeiro nome? ') or 'Nome não digitado.'

if len(name) <= 4:
    print('Nome pequeno!')
elif len(name) <= 6:
    print('Nome médio!')
else:
    print('Nome grande!')
