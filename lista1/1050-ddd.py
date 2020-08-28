# Exercicio: ler int ddd e imprimir de qual cidade e

ddd = int(input())

# cria lista dos nomes das cidades e ddd nas posicoes correspondentes
cities = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']
ddds = [61, 71, 11, 21, 32, 19, 27, 31]

# if-else verifica se ddd esta na listagem
# imprime a cidade conforme a localizacao do ddd
print(cities[ddds.index(ddd)] if ddd in ddds else 'DDD nao cadastrado')
