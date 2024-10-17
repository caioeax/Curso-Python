# Manipulando chaves e valores em dicionários

# pessoa = {
#     'nome': 'Caio Eduardo',
#     'sobrenome': 'Aguiar',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'bal bal', 'numero': 323},
#     ],
# }

pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Caio Eduardo'
pessoa['sobrenome'] = 'Aguiar'

print(pessoa[chave])

pessoa[chave] = 'Isabela'

# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa['sobrenome'])

# print('nao vai ser atingido pois quebrou antes')

# print(pessoa.get('sobrenome', 'Não Existe'))

if pessoa.get('sobrenome') is None:
    print('Não Existe!')
else:
    print(pessoa['sobrenome'])

