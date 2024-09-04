"""
Repetições
while(repetição)
Executa uma ação enquanto uma condição for verdadeira
"""

# condição = True

# while condição:
#     print(1)
#     print(2)
#     print(3)

numberStr = input('Digite quantas vezes rodar: ')
number = int(numberStr)


frase = 'Gustavo é gay'
tamanhoFrase = len(frase)
frase = 'Gustavo é gay' * number
i = 0

while i <= (len(frase) - tamanhoFrase):
    print(frase[0 + i:tamanhoFrase + i])
    i += 1