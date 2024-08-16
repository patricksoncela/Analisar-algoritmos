def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): #cria a função calcular media e aprovação, recebendo como parametros notas e nota minima para aprovação
total_notas = 0 #variavel de valor total das notas recebe 0
num_alunos = len(notas) #variavel de nome dos alunos
aprovados = [] #variavel aprovados recebe um vetor
reprovados = [] #variavel de reprovados recebe um vetor

for aluno, nota in notas.items(): #para cada aluno, pega sua respectiva nota na lista de notas
total_notas += nota #adiciona a nota do aluno ao total das notas
if nota >= nota_minima_aprovacao: #se a nota for maior ou igual a nota minimo para aprovação(70)
aprovados.append(aluno) #adiciona o nome do aluno a lista de aprovados
else: #senão
reprovados.append(aluno) #adiciona o aluno a lista dos reprovados

media_turma = total_notas / num_alunos  #variavel media da turma é calculada dividindo a nota total pelo número de alunos

return media_turma, aprovados, reprovados #retorna os valors de média da turma, aprovados e reprovados a linha 28

notas = {   #lista de notas dos alunos
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

nota_minima_aprovacao = 70  #nota minima para aprovação

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)  #função de calcular media e aprovação é chamada, e e a variavel media da turma, e aprovados e reprovados recebem retorno da função

print(f"Média da turma: {media_turma:.2f}")  #mostra ao usuario a media da turma
print(f"Alunos aprovados: {', '.join(aprovados)}")  #mostra ao usuario os alunos aprovados
print(f"Alunos reprovados: {', '.join(reprovados)}") #mostra ao usuario os alunos reprovados