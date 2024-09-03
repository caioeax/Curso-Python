# Variáveis são usadas para salvar algo na memória
# PEP8: inicie variáveis com letras minusculas, pode usar
# numeros e underlines
# O sinal de = é o operador de atribuição, Ele é usado para
# atribuir um valor a um nome (variável)
# Uso: nome_variavel = expressão.

nome_completo = 'Caio Eduardo de Aguiar'
anoAtual = 2024
idade = anoAtual - 2004
floatVar = 1.1
maiorDeIdade = idade >= 18

print(nome_completo, idade, sep=", ")
print()
print(type(nome_completo), type(idade), type(floatVar), type(maiorDeIdade))
print(nome_completo, idade, floatVar, maiorDeIdade, sep=", ")

print("Você é maior de idade? ", maiorDeIdade)