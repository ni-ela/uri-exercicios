# com N vezes de entrada, imprimir a divisao do par x por y, se erro, printar "divisao impossivel".

#le N (qtde)
n = int(input())

# inicializa lista vazia para servir como print final
result = []

for i in range(0, n): 
    x, y = map(float, input().split())

    #verifica se y é 0, se nao, divide normalmente, em ambos os casos ele inclui o resultado na lista
    result.append('divisao impossivel' if y == 0 else str(x/y))

# imprime todos os itens da lista linha por linha
print(*result, sep='\n')

 # print(*range(len(result))) imprime os indices