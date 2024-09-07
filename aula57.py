"""
Faça uma lista de compras com listas, o usuário deve ter a 
possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de 
indices inexistentes na lista
"""

import os

listaAdd = ''
verify = ''
lista = []
deletar = 0
deletaStr = ''

while True:
    print()
    code = input('Selecione uma opção: \n[i]nserir [a]pagar [l]istar ou [s]air\n').lower()
    if code.startswith('i'):
        os.system('cls')
        listaAdd = input('Escreva o item para colocar na lista. Adicione um item de cada vez.\n')
        lista.append(listaAdd)
    elif code.startswith('a'):
        print()
        deletarStr = input('Qual você deseja deletar? Delete um item de cada vez.\n')
        try:
            deletar = int(deletarStr)
            lista.remove(lista[deletar])
        except IndexError:
            print()
            print('Este índice não existe!')
            continue
        except ValueError:
            print()
            print('Apenas números inteiros!')
            continue
        except Exception:
            print('Erro! Erro não registrado.')
    elif code.startswith('l'):
        os.system('cls')
        if len(lista) < 1:
            print('Nada para listar!')
        else:
            for indice, nome in enumerate(lista):
                print(indice, nome, sep=' - ')
    elif code.startswith('s'):
        break
    else:
        print('Erro na digitação!')

print('Modificações salvas na Lista!')