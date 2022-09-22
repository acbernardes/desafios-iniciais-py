entrada = input().split()

numero_consumido = int(entrada[0])
total_participante = int(entrada[1])

media = float(numero_consumido) / float(total_participante)

print(f'{media:.2f}')