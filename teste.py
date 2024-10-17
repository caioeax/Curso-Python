# # numeros = '123456789'

# # print(int(numeros[1]) - 2)

# # input_bts = input('descreva o membro do bts que eu irei descobrir!!!!!') 

# # print('voce descreveu o jungcock!!!!!!!!!')


# palavra = 'paralelepipedo'
# tamanho_da_palavra = len(palavra)
# criptografia = '' tamanho_da_palavra
# tentativa = 0

# while True:

#     verifica_acerto = palavra == criptografia

#     if verifica_acerto:
#         print(f'parabens, voce acertou a palavra {palavra} em apenas {tentativa} tentativas!!!')
#         break

#     letra_inp = input('digite uma letra: ')
#     mais_de_uma_letra = len(letra_inp)  > 1
#     tentativa += 1

#     if mais_de_uma_letra:
#         print('digite apenas uma letra!!!')
#         continue

#     i = 0 
#     for letra in palavra:
#         if letra_inp == letra:
#             criptografia = criptografia[:i] + letra_inp + criptografia[i+1:]
#         i+=1


import random

lista_aleatoria = []
numeros_apareceram = []
lista_repetidos_organisados = []

for i in range(10):
    aleatorio = random.randint(1, 2)
    lista_aleatoria.append(aleatorio)

x = 0    
y = 0

while True:
    try:
        if lista_aleatoria[y] == lista_aleatoria[x]:
            numeros_apareceram.append(lista_aleatoria[y])
            y+=1
            x = 0   
        else:
            x+=1
    except:
        break
    
    numeros_apareceram.sort()

x = 0
y = None
repetiu = 0
for i in numeros_apareceram:

    try:
        if numeros_apareceram[x] == numeros_apareceram[x + 1]:
            y = i
            repetiu+=1

        elif y == None:
            repetiu = 0
       
        elif numeros_apareceram[x] != numeros_apareceram[x + 1]:
            lista_repetidos_organisados.append(f'{repetiu + 1} {y} = {repetiu + 1} repetições\n')
            y = None
            repetiu = 0
        x+=1
    except:
        break

lista_repetidos_organisados.sort()


for i in lista_repetidos_organisados:
    print(i[i.index(' ')+1:])
print(f'o numero que mais repetiu foi {lista_repetidos_organisados[-1][2:]}')