# ler int N e printar sua tabuada de multiplicacao

# recebe o numero
n = int(input())

# percorre de 1 a 10 multiplicando e exibindo cada item da tabuada
for i in range(1, 11):
    print(i,'x', n, '=', str(n*i))