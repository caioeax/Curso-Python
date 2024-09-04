"""
while/else
"""

string = ' valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        print(i)

    i += 1
else:
    print('Não tem espaço na palavra!')
print('abc') 