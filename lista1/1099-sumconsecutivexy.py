# ler N casos de teste com X e Y, somar 

# n casos
n=int(input())

# inicializa somador do intervalo
sum=0

# inicializa lista vazia para salvar as somas 
result = [] 

for cont1 in range(n): # percorre casos de teste
    # recebe o intervalo
    x, y = map(int,input().split())

    # determina intervalo na ordem de menor para o maior de cada caso
    i = (x if x<y else y) # inicio
    f = (y if x<y else x) # fim
    
    # percorre o intervalo
    for intervalItem in range(i+1, f):
        # verfica se item é impar e soma se true
        if intervalItem%2 != 0:
            sum += intervalItem
    
    result.append(sum)
    sum = 0

# imprime todas as somas dos casos de teste
print(*result, sep='\n')