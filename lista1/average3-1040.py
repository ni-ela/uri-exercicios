# Exercicio: calcula media ponderada, final, exibe situacao do aluno

# recebe as 4 notas uma linha de código
n1, n2, n3, n4 = map(float, input().split())

# calcula a media ponderada
media =  (n1*2 + n2*3 + n3*4 + n4)/10

# imprime a media conforme o ponto flutuante 1 requisitado
print('Media: %.1f' % media)

# exibe situacao do aluno conforme a media
if media >= 7: print('Aluno aprovado.')
elif media < 5: print('Aluno reprovado.')
elif media >= 5 and media <= 6.9: 
    print('Aluno em exame.') 

    # recebe nota do exame em caso de aluno em exame final
    notaExame = float(input())
    print('Nota do exame: %.1f' % notaExame) 

    # calcula media final
    media = (media + notaExame)/2

    # exibe situacao final do aluno
    if media >= 5: print('Aluno aprovado.')
    elif media <= 4.9: print('Aluno reprovado.')
    print('Media final: %.1f' % media)