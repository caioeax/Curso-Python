import random




while True:
    trueCpf = ''
    cpfInput = ''
    tamanhoCpf = 0
    i = 0
    j = 0
    index_2 = 0
    valorMulti = 0
    for i in range(11):
        cpfInput += str(random.randint(0, 9))
    # cpfInput = input('CPF: ')  
    print()

    trueCpf = cpfInput.replace(".","").replace("-","") 
    # trueCpf = re.sub(r'[^0-9]', '', cpfInput)
    tamanhoCpf = len(trueCpf)

    if tamanhoCpf > 11 or tamanhoCpf < 11:
        print('Erro! CPF incorreto.')
        break

    index_2 = 10

    while i < tamanhoCpf - 2:
        valorMulti = valorMulti + int(trueCpf[i]) * index_2
        i += 1
        index_2 -= 1

    valorMultiFinal_1 = valorMulti * 10
    verifyCpf = valorMultiFinal_1 % 11

    if verifyCpf == 10:
        verifyCpf = 0
    
    if verifyCpf == int(trueCpf[9]):
        index_2 = 11
        valorMulti = 0

        while j < tamanhoCpf - 1:
            valorMulti = valorMulti + int(trueCpf[j]) * index_2
            j += 1
            index_2 -= 1

        valorMultiFinal_2 = valorMulti * 10
        verifyCpf2 = valorMultiFinal_2 % 11

        if verifyCpf2 == 10:
            verifyCpf2 = 0
        if verifyCpf2 == int(trueCpf[10]):
            print(f'Cpf válido. CPF: {cpfInput}')
            break
        else:
            print('CPF digitado incorretamente!')
            continue
    else:
        print('CPF digitado incorretamente!')
        continue