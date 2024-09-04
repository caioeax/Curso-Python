"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- COntagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máximo do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

# if velocidade > RADAR_1:
#     print('Velocidade carro passou do radar 1')

# if local_carro >= (LOCAL_1 + RADAR_RANGE) and local_carro <= (LOCAL_1 - RADAR_RANGE) and velocidade > RADAR_1:
#     print('carro multado em radar 1')
# else:
#     print('Tudo certo chefia!')

veloCarroRadar1 = velocidade > RADAR_1
carroPassouRadar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carroMultadoRadar1 = carroPassouRadar1 and veloCarroRadar1

if veloCarroRadar1:
    print('Velocidade carro passou do radar 1')

if carroPassouRadar1:
    print('Carro passou aqui, guys')

if carroMultadoRadar1:
    print('carro multado em radar 1')
else:
    print('Tudo certo chefia!')
