# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool.
print(1 + 1) # somando números
print("a" + "b") # somando strings, na verdade foi concatenado.

# print('1' + 1) # não pode concatenar str com int.
print('1', type('1')) # mostrando o tipo "str no caso".
print(int('1'), type(int('1'))) # mostrando o tipo "int no caso".
print(int('1') + 1) # transformando uma string em um int para somar com um int.
print(float('1') + 1) # transformando uma string em um float para somar com um int.
print(type(float('1') + 1)) # checar o type.
print() # \n

print(bool(' ')) # tem qualquer coisa dentro -> true
print(bool('')) # não tem coisa dentro -> 
print()

# print(11 + 'b') # erro
print(str(11) + 'b') # transformando um int para string para concatenar duas strings.