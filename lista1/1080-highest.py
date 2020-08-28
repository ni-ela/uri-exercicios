# ler 100 inteiros e imprimir o maior valor e sua posicao
list = []

# percorre de 1 a 100 e salva os numeros
for i in range(0, 100):
    n = int(input())
    list.append(n)

# verifica o maior
maior=max(list)

#imprime-o e seu indice
print(maior,list.index(maior)+1, sep='\n')




#print(len(list))
#randint(1,100)
#from random import *




