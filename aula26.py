"""
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
(Caractere)(><^)(quantidade)
> - Esquerda
> - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.5932618975621387695:,.1f}')
print(f'{1000.5932618975621387695:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')