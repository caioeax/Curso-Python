# Exercícios
# Crie funções que duplicam, triplicam, quadruplicam
# o número recebido como parâmetro

# def multiplicador(x):
#     var1 = number * 2
#     var2 = number * 3
#     var3 = number * 4
#     return f'Seu número duplicado é {var1}, Seu número triplicado é {var2}, Seu número quadruplicado é {var3}'

# number = int(input('Digite o numero! '))
# resposta = multiplicador(number)
# print(resposta)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2) # Estou definindo o multiplicador, ou seja, esse é duplo
triplicar = criar_multiplicador(3) # Estou definindo o multiplicador, ou seja, esse é triplo
quadruplicar = criar_multiplicador(4) # Estou definindo o multiplicador, ou seja, esse é quadruplo
print(duplicar(20)) # Estou falando para duplicar o número 20
print(triplicar(20)) # Estou falando para triplicar o número 20
print(quadruplicar(20)) # Estou falando para quadruplicar o número 20
