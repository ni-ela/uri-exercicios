# Exercicio 1160: imprimir, para cada caso de teste, quantos anos seriam necessários para que a cidade A se tornasse maior que a cidade B (em habitantes). 

# recebe qtde de casos de teste
t = int(input())

# listagem dos anos
anos = []

# contador de anos
tempo = 0

# salva os casos de teste
for i in range (t):

    # qtde da populacao e respectivos crescimentos populacionais (%)
    pa, pb, g1, g2 = map(float, input().split())

    # o laco atualiza os valores ate pa alcancar pb
    while pa <= pb:

        # reutiliza as variaveis pa e pb de modo a transforma-las em taxas de crescimento
        pa = int((1+g1/100)*pa)
        pb = int((1+g2/100)*pb)
        tempo += 1 # enquanto a condicao nao é satisfeita, incrementa-se 1 ano

        # verfifica e aplica break para evitar tempo limite excedido 
        if tempo > 100:
            break

    # listagem recebe o resultado do caso de teste i (atual),
    # if tempo é nao ultrapassa 100 anos, a qtde de anos sera exibida
    # caso contrario, 'Mais de 1 seculo' sera registrado
    anos.append(str(tempo) + ' anos.' if tempo <= 100 else 'Mais de 1 seculo.')
    
    # reinicia contador
    tempo = 0

# imprime a analise de cada caso
print(*anos, sep='\n')