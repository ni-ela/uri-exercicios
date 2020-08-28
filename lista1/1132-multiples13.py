# ler X e Y e somar todos os do intervalo que nao sao divisiveis por 13

# recebe o inicio e fim (x,y) do intervalo
x = int(input())
y = int(input())

# inicializa somador
sum=0

# com operador ternário, verfifica qual o inicio e fim na ordem de menor para o maior
i = (x if x<y else y)
f = (y if x<y else x)

# percorre o intervalo
for j in range(i, f+1):

    # verfiica se não é multiplo de 13
    if j%13 != 0:
        sum += j

# printa a saida esperada
print(sum)