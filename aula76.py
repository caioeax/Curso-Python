"""
Dicionarios em python (dict)
dicionarios são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "indice"
que vimos na lista e podem ser de tipos imutáveis
como str int float bool tuple etc
o valor pode ser de qualquer tipo, incluindo outro dicionario
usamos as chaves - {} - ou a classe dict para criar dicionarios
imutaveis: str int float bool tuple
mutavel: dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'bal bal', 'numero': 323},
        {'rua': 'dal dal', 'numero': 543},
    ]
}
"""

# pessoa = dict(nome='Caio Eduardo', sobrenome='Aguiar')

pessoa = {
    'nome': 'Caio Eduardo',
    'sobrenome': 'Aguiar',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'bal bal', 'numero': 323},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['idade'])
print(pessoa['altura'])

print()

for chave in pessoa:
    print(chave)