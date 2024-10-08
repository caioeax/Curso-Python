"""
Iterável -> str, range, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
texto = iter('Caio') # ___iter___ (iteravel)
iterador = iter(texto) # (iterador)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)