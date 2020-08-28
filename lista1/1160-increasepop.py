# Exercicio: imprimir, para cada caso de teste, quantos anos seriam necessários para que a cidade A se tornasse maior que a cidade B (em habitantes). 

Preste atenção, por favor: A população é sempre um número inteiro. Portanto, um crescimento d
e 2,5% sobre uma população de 100 resultará em 102 (em vez de 102,5) e um crescimento de 2,5% sobre
 uma população de 1000 resultará em 1025. Além disso, use variáveis ​​duplas para a taxa de crescimento.

Resultado
Lembre-se que se este tempo for maior que 100 será necessário 
imprimir a mensagem: "Mais de 1 segundo". Em cada um desses casos, talvez seja interessante interromper 
a contagem, caso contrário você obterá "Limite de tempo excedido".



# recebe qtde de casos de teste
t = int(input())

# anos
anos = []

for i in range (t):
    pa = int(input())
    pb = int(input())
    
    #respectivos crescimentos populacionais (%)
    g1 = int(input())
    g2 = int(input()) # com um dígito após a vírgula

    cresca = pa * g1 + pa
    crescb = pb * g2 + pa

    cres
    print('%.0f' % cresc)
    anos.append()