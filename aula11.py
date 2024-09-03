# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta1 = 1 + 1 ** 5 + 5 # 1024 teoricamente -> 1^5 = 1 -> 1 + 1 + 5 = 7
print(conta1)

print()

# Mudar o valor da mesma variável.
conta1 = (1 + 1) ** (5 + 5) # 1024 funcionando - > 1 + 1 = 2 e 5 + 5 = 10 - > 2^10 = 1024
print(conta1)