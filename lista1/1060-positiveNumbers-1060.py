#Exercicio: Receber 6 numeros e printar quantos sao positivos.

#recebe as 6 entradas
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

#cria lista para trabalhar com os numeros em grupo
numbers= [n1,n2,n3,n4,n5,n6]

#cria contador de numeros positivos
countNumber=0

#percorre de numero em numero na lista
for number in numbers:
    #verifica se numero é positivo
    if number>0: countNumber+=1
#printa a qtde de valores positivos
print(countNumber, 'valores positivos')
