valores = input().split()
GASTO = 12

tempo = int(valores[0])
velocidade = int(valores[1])

distancia = velocidade*tempo

litros = float(distancia) / float(GASTO)

print(f'{litros:.3f}')