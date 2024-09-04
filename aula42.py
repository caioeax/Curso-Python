frase = 'O Python é uma linguagem de programação multiparadigma Python foi criado por Guido van Rossum.'.lower()

i = 0
verify = 0

while i < len(frase):
    letra = frase[i]
    numeroLetra = frase.count(frase[i])
    i += 1

    if letra == ' ':
        continue

    if verify < numeroLetra:
        verify = numeroLetra
        letraFinal = letra


print(f'A letra que mais apareceu foi a letra "{letraFinal}", tendo aparecido um total de {verify} vezes.')