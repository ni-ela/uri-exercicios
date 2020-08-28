# Exercicio 1155: ler n entradas e dizer se cada e ou nao numero perfeito

casos = int(input())

# inicializa lista vazia para salvar as somas 
result = [] 

for cont1 in range(casos): # percorre casos de teste

    # inicializa/zera somador dos divisores do numero
    sum=0
    
    # recebe o numero
    n = int(input())

    # percorre de 1 a n-1
    for antecessor in range(1, n):
        # verifica se antecessor é divisor de n
        if n%antecessor == 0:
            sum += antecessor
    
    result.append('%d eh perfeito' % n if sum==n else '%d nao eh perfeito' % n)

# imprime todas as verificacoes dos casos de teste
print(*result, sep='\n')