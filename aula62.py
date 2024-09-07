# Desempacotamento em chamadas
# de métodos e funções

string = 'abcd'
lista = ['Caio', 'é', 1, 2, 3, 'Eduardo']
tupla = 'python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Caio', 'é', 1, 2, 3, 'Eduardo')
# print(*lista)
# print(*string)
# print(*tupla)

print(*lista, sep='\n')