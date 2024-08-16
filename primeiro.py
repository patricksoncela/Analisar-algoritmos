# coding=utf-8
def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): #função para calcular os juros com atraso, recebe como parametros: valor_principal, taxa_juros_anual, e dias_atraso.
    taxa_juros_diaria = taxa_juros_anual / 365 / 100 #var que pega o valor dos juros anuais(5) e divide obtendo a taxa de juros por dia

    juros = valor_principal * taxa_juros_diaria * dias_atraso #var total dos juros que multiplica o valor principal(1000) pela taxa de juros ao dia(5/365/100), pelos dias em atraso(3)

    valor_total = valor_principal + juros #var que calcula o valor total
    return valor_total, juros #retorna a linha 12, os valores de valor_total e juros

valor_principal = 1000.00  #var com o valor principal sem juros algum
taxa_juros_anual = 5.0  #var com a taxa de juros por ano
dias_atraso = 30 #var que mostra o número de dias de atraso
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso) #chama a função calcular_juros_atraso, mandando como parametro o valor principal, a taxa de juros anual e os dias em atraso, e obtendo o valor total e valor dos juros
print(f'Valor total a ser pago: R${valor_total:.2f}') #mostra ao usuário o valor total a pagar
print(f"Valor dos juros: R${juros:.2f}") #mostra ao usuário o valor dos juros