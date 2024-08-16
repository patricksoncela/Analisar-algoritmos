# coding=utf-8
def calcular_imc(peso, altura): #cria a função calcular_imc que recebe como parametros peso e altura

imc = peso / (altura ** 2) #calcula o imc pela divisão do peso, pela altura*2
return imc #retorna o valor de imc

def classificar_imc(imc): #cria a função classificar_imc que utiliza como parametro o valor de imc obtido na função anterior

if imc < 18.5: #se o imc é menor que 18,5
return "Abaixo do peso" #retorna abaixo do peso
elif 18.5 <= imc < 24.9: #se imc for menor que 24.9 e maior ou igual a 18.5
return "Peso normal" #retorna peso normal
elif 25 <= imc < 29.9: #se imc for menor que 29.9 e maior ou igual a 25
return "Sobrepeso" #retorna sobrepeso
elif 30 <= imc < 34.9: #se imc for menor que 34.9 e maior ou igual a 30
return "Obesidade grau 1" #retorna obesidade grau 1
elif 35 <= imc < 39.9: #se imc for menor que 39.9 e maior ou igual a 35
return "Obesidade grau 2" #retorna obesidade grau 2
else: #em outro caso
return "Obesidade grau 3" #retorna obesidade grau 3

def sugestao_atividade_fisica(classificacao_imc): #cria a função sugerir atividade física usando como parametro a classificação do imc obtida na função anterior

if classificacao_imc == "Abaixo do peso": #se a classificação do imc for igual a abaixo do peso
return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em
proteínas e calorias." #sugere fortalecimento muscular e dieta rica em proteinas e calorias
elif classificacao_imc == "Peso normal": #se a classificação for peso normal
return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e
natação, junto a um treino de força moderado." #sugere atividades aerobicas e treino de força moderado
elif classificacao_imc == "Sobrepeso": #se a classificação for sobrepeso
return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além
de exercícios de resistência." #sugere atividades aerobias e exercicios de resistencia
elif classificacao_imc == "Obesidade grau 1": #se a classificação for obesidade grau 1
return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um
programa de reeducação alimentar." #sugere atividades de baixo impacto e programa de reeducação alimentar
elif classificacao_imc == "Obesidade grau 2": #se a classificação for obesidade grau 2
return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e
acompanhamento nutricional." #sugere exercicios de baixo impacto com supervisão e acompanhamento nutricional
else: #caso contrário
return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica,
fisioterapia, e consultas regulares com um nutricionista." #sugere atividades físicas supervisionadas por profissionais e consulta a nutricionistas

peso = float(input("Digite seu peso (em kg): ")) #variavel peso recebe valor float por input
altura = float(input("Digite sua altura (em metros): ")) #variavel altura recebe valor float por input

imc = calcular_imc(peso, altura) #chama função calcular imc e recebe o valor de imc
classificacao_imc = classificar_imc(imc) #chama a função classificar_imc e recebe o valor de classificacao_imc
sugestao = sugestao_atividade_fisica(classificacao_imc) #chama a função sugestao atividade fisica e recebe o valor de sugestao

print(f"Seu IMC é: {imc:.2f}" #mostra o imc ao usuario
print(f"Classificação: {classificacao_imc}") #printa a classificação
print(f"Sugestão de atividade física: {sugestao}") #printa a sugestao