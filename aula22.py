# Operadores Lógicos, and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso. a expressão inteira
# será avaliada naquele valor.
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar não valor.

# entrada = input('[E]ntrar | [S]air\n')
# senhaDigitada = input('Senha: ')

# senhaPermitida = '123456'
# if (entrada == 'E' or entrada == 'e') and senhaDigitada == senhaPermitida :
#     print('Você entrou!')
# elif (entrada == 'E' or entrada == 'e') and senhaDigitada != senhaPermitida :
#     print('Senha incorreta!')
# elif (entrada == 'S' or entrada == 's') :
#     print('Você saiu!')
# else :
#     print('Erro!')

# Avaliação de Curto Circuito

# print(True and 0 and True)
# print(True and False and True)
# if 0 and 1:
#     print(True and 1)
# print(bool(''))

senha = input('Senha: ') or 'Sem Senha'
print(senha)