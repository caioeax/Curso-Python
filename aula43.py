# texto = 'Python'

# i = 0
# tamanhoString = len(texto)

# while i < tamanhoString:
#     print(texto[i], i)

#     i += 1

# senhaSalva = '123456'
# senhaDigitada = ''
# repeticoes = 0

# while senhaSalva != senhaDigitada:
#     senhaDigitada = input(f'Sua senha ({repeticoes}x)')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

texto = 'Python'

novoTexto = ''
for letra in texto:
    novoTexto += f'*{letra}'
    # print(letra)
print(novoTexto + '*')