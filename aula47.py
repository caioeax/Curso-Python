"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavraSecreta = 'dhruv'
letraAcertada = ''
letrasChutadas = ''
tentativas = 0

while True:
    if tentativas == 0:
        print()
        print('Dica: Famoso')

    letraDigitada = input('Escreva uma letra: ')

    if len(letraDigitada) > 1:
        print('Apenas uma letra!')
        continue

    if letraDigitada in letrasChutadas:
        print('Você já chutou essa letra!')
        continue

    letrasChutadas += letraDigitada

    tentativas += 1

    if tentativas == 5:
        print()
        print('Faz musica!')

    if tentativas == 10:
        print()
        print('Voce conhece!')
    
    if letraDigitada in palavraSecreta:
        letraAcertada += letraDigitada

    palavraFormada = ''
    for letraSecreta in palavraSecreta:
        if letraSecreta in letraAcertada:  # Corrigido para verificar se a letra está na string letraAcertada
            palavraFormada += letraSecreta
        else:
            palavraFormada += '*'

    print(palavraFormada)

    if palavraFormada == palavraSecreta:
        print('Parabéns! Você ganhou!')
        print(f'A palavra era {palavraSecreta}')
        print(f'Você conseguiu em {tentativas} tentativas.')
        break  # Corrigido para encerrar o loop
