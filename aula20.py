primeiroValor = input('Digite um valor: ')
segundoValor = input('Digite outro valor: ')

if primeiroValor < segundoValor :
    print(f'O {segundoValor=} é maior do que o {primeiroValor=}')
elif segundoValor < primeiroValor :
    print(f'O {primeiroValor=} é maior do que o {segundoValor=}')
else :
    print(f'O dois valores são iguais, sendo eles: {primeiroValor}')

