a = 'AaAa'
b = 'BbBb'
c = 1.101
# formato = 'a={} b={} c={}'.format(a, b, c)
formato = 'a={nome1} b={nome2} c={nome3}'.format(
     nome1=a, nome2=b, nome3=c
)
# formato = '{0} {1} {2}'
# print(formato.format(a, b, c))
# formato = 'a={} b={} c={} {}'.format(a, b, c) # out of range ta pedindo 4 e só tem 3.

print(formato)