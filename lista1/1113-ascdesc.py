# ler pares x,y e imprimir se crescente ou decrescente, a entrada finaliza quando x=y

message = []
x= 0
y= 1
while (x!=y):
    x, y = map(int,input().split())
    # salva analise da ordem dos numeros
    if x!=y: message.append('Crescente' if x<y else 'Decrescente')

# imprime a analise de cada caso
print(*message, sep='\n')