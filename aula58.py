"""
Imprecisão de ponto flutuante
"""

import decimal

numero1 = decimal.Decimal(0.1) # Deveria recorrer um erro, pois 0.1 não é decimal!
numero2 = decimal.Decimal(0.7) # Deveria recorrer um erro, pois 0.1 não é decimal!
numero3 = numero1 + numero2

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2

numero1 = decimal.Decimal('0.1') 
numero2 = decimal.Decimal('0.7') 
numero3 = numero1 + numero2

print(numero3) # número que pode ter a imprecisão
print(f'{numero3:.2f}') # formatando o número
print(round(numero3, 1)) # usando o arredondamento