"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condicao for verdadeira
Loop infinito -> quando um codigo nao tem fim
"""
# contador = 0

# while contador <= 10:
#     contador += 1
#     print(contador)

#     if contador == 6:
#         print('Não vou mostrar o 6')
#         continue

#     if contador == 10:
#         break

contadorStr = input("Até qual número ir?")
contador = int(contadorStr)
i = 0

while i < contador:
    i += 1

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)