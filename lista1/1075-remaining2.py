# ler int N e imprimir todos os numeros de 1 a 10000 que dividos por n resta 2

#le N
n = int(input())

#percorre de 1 a 10000
for number in range(0, 10001): 

    #imprime a saida desejada
    if number%n == 2: 
        print(number)