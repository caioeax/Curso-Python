# Tipos int e float
# int > Numero inteiro
# O tipo int representa qualquer número
# positivo ou negativo, sem sinal é positivo.
print(11,) # int
print(-11,) # int
print(0,) # int
print() # \n

# float > número com ponto flutuante
# O tipo float representa qualquer número 
# positivo ou negativo com ponto flutuante.
# float sem sinal é positivo.
print(1.1, 10.11, sep=" e ") # float
print(-1.1, -10.11, sep=" e ") # float
print(0, -0, sep=" e ") # float
print() # \n

# A função type mostra o tipo que o Python
# inferiu ao valor.

print(type('Eduardo'), type("Eduardo"), type("""Eduardo"""))
print(type(1), type(-1), type(0))
print(type(-1.1), type(1.1), type(0.0))