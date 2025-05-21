numeros = []


for i in range(5):
     numero = float(input(f"digite os {i+1}º numero:"))
     numeros.append(numero)

nova_lista = [num * 2 for num in numeros]

print("Primeira lista: ", numeros)
print("Nova lista:" , nova_lista)

soma_primeira_lista = sum(numeros)
soma_nova_lista = sum(nova_lista)

print("Soma dos numeros na primeira lista: ", soma_primeira_lista)
print("Soma dos numeros na nova lista: ", soma_nova_lista)