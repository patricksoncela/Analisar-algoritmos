# coding=utf-8
def calcular_area_comodos(): #função que calcula a area dos comodos
    total_area = 0

    while True: #Mantém o loop rodando enquanto a variavel mais_comodos for igual a "s" (linha 15 até 17)

        largura = float(input("Digite a largura do cômodo (em metros): ")) #var largura recebe a largura(float) de um comodo por input do usuário
        comprimento = float(input("Digite o comprimento do cômodo (em metros): ")) #var comprimento recebe o comprimento(float) de um comodo por input do usuário

        area_comodo = largura * comprimento #var area_comodo recebe a área do comodo multiplicando largura e comprimento
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") #área do cômodo é apresentada ao usuário

        total_area += area_comodo #var área total soma o resultado da area do comodo, a área total ja presente na variável

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()  #pergunta ao usuário se deseja calcular a área de mais comodos e atribui o valor da resposta a variavel mais_comodos
        if mais_comodos != 's':  #se a variavel for diferente de "s"
        break #o loop é encerrado e a área total é mostrada

    return total_area #retorna o valor de área total a linha 21, encerrando a função

area_total = calcular_area_comodos() #chama a função calcular_area_comodos() sem parametros e recebe dela o valor de área total
print(f"A área total da casa é: {area_total:.2f} metros quadrados.") #mostra ao usuário a área total da casa.