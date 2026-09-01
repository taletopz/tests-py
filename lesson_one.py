distancia = int(input("Digite um número pra somar todos os anteriores: "))

soma = 0

for i in range(1, distancia + 1):
    soma = soma + i

print(soma)