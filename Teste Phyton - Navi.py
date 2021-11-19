import math 

#Primeira Questão 
satisfaz = 0
i = 1
maximo = 5000000
while i <= maximo:
    if (i%2==0) and (i%49==0) and (i%37==0):
        satisfaz += 1
    i+=1
print("Há exatamente {0} numeros entre 1 e 5 milhões que satisfazem as 3 condições (Par, múltiplo de 49 e múltiplo de 37)".format(satisfaz) )

#Segunda Questão
vetor = [0]*10
for i in range(len(vetor)):
    if i%2==0:
        vetor[i] = 3**i + 7* (math.factorial(i))
    else:
        vetor[i] = 2**i + 4*math.log(i)

valor_maximo = max(vetor)
indice_maximo = vetor.index(valor_maximo)
media = sum(vetor)/len(vetor)

print('A posição do maior elemento dessa lista é: {0} e a média dos elementos contidos é: {1:.2f}'.format(indice_maximo, media))


#Terceira Questão
nota_cinco = {}
nota_1 = input ('Insira a nota do aluno 1: ')
nota_cinco['Aluno_1'] = nota_1
nota_2 = input ('Insira a nota do aluno 2: ')
nota_cinco['Aluno_2'] = nota_2
nota_3 = input ('Insira a nota do aluno 3: ')
nota_cinco['Aluno_3'] = nota_3
nota_4 = input ('Insira a nota do aluno 4: ')
nota_cinco['Aluno_4'] = nota_4
nota_5 = input ('Insira a nota do aluno 5: ')
nota_cinco['Aluno_5'] = nota_5

maior = max(nota_cinco.values())
for nome, nota in nota_cinco.items():
    if nota==maior:
        print('A pessoa de maior nota é o {0}, com {1} de nota'.format(nome,nota))



    

