# coding=utf-8
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): #cria a função diagnosticar_diabetes, passando os parametros: glicemia em jejum e glicemia pos prandial

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: #Se a glicemia em jejum do paciente for maior ou igual a 126 ou a glicemia pos prandial for maior ou igual a 200
        return "Diabetes" #retorna "diabetes" como conteúdo da variável resultado
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200: #Se a glicemia em jejum do paciente é maior ou igual a 100 e menor do que 126, ou se a glicemia pos prandial for maior ou igual a 140 e menor que 200
        return "Pré-diabetes" #retorna "pré-diabetes" como conteúdo da variável resultado
    else: #em outro caso
        return "Normal" #retorna "normal" como valor da variavel resultado

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) #recebe o valor da glicemia em jejum pelo input do usuário
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): ")) #recebe o valor da glicemia pos prandial como input do usuário

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial) #chama a variável diagnosticar_diabetes com glicemia em jejul e glicemia pos prandial como parametros, e recebe como retorno, o valor da variavel resultado
print(f"O diagnóstico é: {resultado}")  #printa o diagnóstico ao usuário