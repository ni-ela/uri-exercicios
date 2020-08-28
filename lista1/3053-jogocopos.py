# Exercicio: dizer a pos final da moeda

# recebe qtde de jogadas
nplays = int(input())

# posicao atual da moeda, no caso, a inicial
pos = input()

# recebe os comandos
for i in range (nplays):
    command = int(input())

    # os ifs trocam a pos atual conforme o comando

    if command == 1:
    # 'se moeda esta em pos A, trocar para pos B'. Caso ocorrer o inverso a logica faz a devida troca
        if  pos == 'A':
            pos = 'B'
        elif pos == 'B':
            pos = 'A'
    
    if command == 2:
        if  pos == 'B':
            pos = 'C'
        elif pos == 'C':
            pos = 'B'
    
    if command == 3:
        if  pos == 'C':
            pos = 'A'
        elif pos == 'A':
            pos = 'C'

print(pos)





