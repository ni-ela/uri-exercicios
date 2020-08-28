# Exerício: ler N numeros e imprimir quais estao no intervalo [10,20]

#le N
n = int(input())

# contadores de numeros dentro e fora do intervalo
inside=0
outside=0

for i in range(0,n): 
    number = int(input())
    #verifica se está entre 10 e 20
    if number > 9 and number < 21:
        #incrementa na qtde de numeros dentro
        inside += 1

        #incrementa na qtde de numeros fora
    else: outside += 1 

#imprime conforme a saida desejada
print(inside, 'in')
print(outside, 'out')
