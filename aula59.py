"""
split e join com list e str
split - divide uma string
join - junta uma string
"""

frase = 'Olha só que, interessante esse recurso'
listaFraseCruas = frase.split(",")

listaFrases = []

for i, frase in enumerate(listaFraseCruas):
    listaFrases.append(listaFraseCruas[i].strip())

# print(listaFraseCruas)
# print(listaFrase)

frasesUnidas = ' '.join(listaFrases) # numeros nao da
print(frasesUnidas)