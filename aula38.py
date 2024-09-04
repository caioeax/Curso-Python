"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condicao for verdadeira
Loop infinito -> quando um codigo nao tem fim
"""

qtdLinhas = 5
qtdColunas = 5

linha = 1

while linha <= qtdLinhas:
    coluna = 1
    
    while coluna <= qtdColunas:
        print(f'{linha=} {coluna=}')
        coluna += 1

    print()
    linha += 1