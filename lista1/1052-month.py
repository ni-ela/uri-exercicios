# Exerício: imprimir o nome do mês a partir do numero informado
# recebe o mes em numero
month = int(input())

# cria lista dos nomes dos meses
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# verifica se o mês é valido (se é um numero entre 1 e 12) e, em seguida, imprime o item da lista
# que tem indice correspondente ao numero informado -1 (obs: o -1 foi utilizado porque a lista tem indice que vai de 0 a 11)
if month > 0 and month < 13: print(months[month-1])