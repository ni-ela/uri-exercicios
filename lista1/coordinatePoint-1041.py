# Exercicio: receber as coordenadas x e y de um ponto e informar se esta no eixo x, y, na origem ou em qual quadrante

# recebe as coordenadas (x,y) do ponto em uma linha de código
x, y = map(float, input().split())

# com o operador condicional if disposto de uma forma semelhante ao ternário da linguagem C, por exemplo,
# atribui se o ponto esta no eixo x ou y 
point = 'Eixo Y' if x == 0 and y!=x else 'Eixo X'

# verifica se o ponto esta na origem e atribui tal valor
if(x == y == 0): point='Origem'

# verifica em qual quadrante o ponto esta
elif x<0 and y>0: point='Q2'
elif x>0 and y>0: point='Q1'
elif x>0 and y<0: point='Q4'
elif x<0 and y<0: point='Q3'

# Para garantir que o programa forneca uma unica saida atendendo apenas uma das condicoes anteriores,
# utilizou-se a variavel point 
print(point)