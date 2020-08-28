
#  for number in range(1,101): print(number if number%2==0 else ' ', end='')

#Exercicio: imprimir numeros pares de 1 a 100

# percorre de numero em numero desde o 1 ate o 101 (obs: 101 para considerar o 100 na contagem)
for number in range(1,101): 
    # verifica se numero é par. Se sim, imprime-o 
    if number%2==0:
        print(number)