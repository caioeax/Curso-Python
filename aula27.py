"""
Fatiamento de strings
 012345678
 Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
OBS.: a função len  retorna a qtd de caracteres da str
"""

variavel = 'Olá Mundo'
print(variavel[0:3]) # pega do O até o á -> Olá
print(variavel[4:]) # pega do M até o fim -> Mundo

print(len(variavel)) # tamanho
print(variavel[0:len(variavel)]) # do O até a len da variável, logo 9 -> 0:9 -> Olá Mundo
print(variavel[0:9:1]) # Pegando um por vez -> Olá mundo
print(variavel[0:9:2]) # Pegando dois por vez -> OáMno
print(variavel[0:9:3]) # Pegando tres por vez -> O n
print(variavel[0:9:-1]) # nao vai mostrar nada, pois nao da pra ir pra trás.
print(variavel[::-1]) # inverti a String
print(variavel[-1:-10:-1]) # Outro jeito de inverter a String