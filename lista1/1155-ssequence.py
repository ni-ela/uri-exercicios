# Exercicio 1155: calcular e imprimir o valor de S = 1 + 1/2 + 1/3 + … + 1/100

# inicializa S com o primeiro valor
s=1

# percorre os denominadores e incrementa-os
for i in range(2, 101):
    s += 1/i

print('%.2f' % s)