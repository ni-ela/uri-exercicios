# This N is the size of a array X[N]. Next, read each of the numbers of X, find the smallest element of this array and its position within the array, printing this information.

list = []
n = int(input())

# percorre de 0 a n e salva os numeros
for i, v in range(0, n):
    list = [map(int,input())]
    for indice, valor in enumerate(lista):
    print "lista[%d] = %d" % (indice, valor)

    #list.append(int(input()))

# verifica o menor
menor=min(list)

#imprime-o e seu indice
print('Menor valor: %d' % menor) 
print('Posicao: %d' % list.index(menor))
#print(menor,list.index(menor)+1, sep='\n')