# ler int X e Y e imprimir todos os números entre X e Y que dividido por 5 o resto é igual a 2 ou igual a 3

# recebe inicio e fim do intervalo
x =int(input())
y =int(input())

# com operador ternário, verfifica qual o inicio e fim na ordem crescente
i = (x if x<y else y)
f = (y if x<y else x)

# O percorre, verifica valores e imprime conforme a sada esperada
for i in range(i+1, f):
    if i%5==3 or i%5==2:
        print(i)
# verifica se o ponto esta na origem e atribui tal valor
if(x == y == 0): point='Origem'

# verifica em qual quadrante o ponto esta
elif x<0 and y>0: point='Q2'
elif x>0 and y>0: point='Q1'
elif x>0 and y<0: point='Q4'
elif x<0 and y<0: point='Q3'