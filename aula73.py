"""
Higher order function
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'Bom dia', 'Caio'))
print(executa(saudacao, 'Bom dia', 'Maria'))

# v= saudacao('bom dia')
# print(v)

