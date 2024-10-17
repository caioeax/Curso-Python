# Exercícios com funções

"""
Crie uma função que multiplica todos os argumentos
"""

"""
Crie uma fução fala se um número é par ou ímpar
Retorne se é par ou impar
"""

# def operacao (*args):
#     conta = 1
#     for numero in args:
#         conta *= numero
#     return conta

# multi = operacao(6, 8, 3, 4, 2)
# print(multi)

def verify(x):
    if x % 2 == 0:
        return 'Par!'
    return 'Ímpar!'

number = int(input('Digite o número para verificação! '))
answer = verify(number)
print('Seu número é', answer)