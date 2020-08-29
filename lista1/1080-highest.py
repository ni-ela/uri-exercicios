# Exercicio 1080: ler 100 inteiros e imprimir o maior valor e sua posicao

maior = 0
pos = 0

# percorre de 1 a 100 e salva os numeros
for i in range(0, 100):
    n = int(input())


    # verifica o maior comparando entrada atual com anterior
    maior = n if n > maior else maior
    pos = i if maior == n else pos

print(maior, pos)




## Outra forma usando lista:

# maior=max(list)

## imprime-o e seu indice

# print(maior,list.index(maior)+1, sep='\n')




#print(len(list))
#randint(1,100)
#from random import *




