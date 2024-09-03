nome = 'Caio Eduardo'
altura = 1.80
peso = 80
imc = ... # IMC = peso / (altura x altura)

imc = peso / (altura * altura) # ou peso / altura ** 2
frase1 = f"{nome} tem {altura:.2f}cm," # precisa do f para formatar as variáveis.
frase2 = f"pesa {peso} kg e seu IMC é: {imc:.2f}"
print(frase1)
print(frase2)

# ou 
# print(frase1, frase2)