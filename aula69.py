"""
Escopo de funções em Pyrhon
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1

def escopo():
    global x
    x = 10

    def outraFuncao():
        x = 11
        y = 2
        print(x + y, "-> outra Função")
    # x = 1
    outraFuncao()
    print(x, "-> escopo")


# print(x) # Não funciona pois x está localizado num escopo local.

print(x)
escopo()
print(x)
