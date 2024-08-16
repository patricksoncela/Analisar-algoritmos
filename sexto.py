def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio):  #cria a função calcular custo de viagem, recebe como parametros: distancia, custo do combustiel, consumo do veiculo, numero de pedagios e custo do pedagio

custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel #calcula o valor do custo do combustivel total pela divisão da distancia pelo consumo do veiculo, multiplicado pelo custo do combustivel

custo_pedagio_total = numero_pedagios * custo_pedagio #calcula o valor do pedagio total, multiplicando o numero de pedagios pelo valor

custo_total = custo_combustivel_total + custo_pedagio_total #calcula o custo total somando o valor total de combustivel com o custo de pedagio total

return custo_total, custo_combustivel_total, custo_pedagio_total #retorna o valor do custo total, custo de combustivel total, e custo de pedagio total encerrando a função

distancia = float(input("Digite a distância da viagem (em km): ")) #var distancia recebe valor float por input do usuario
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): ")) #var custo combustivel recebe valor float por input
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): ")) #var consumo veiculo recebe valor float por input do usuario
numero_pedagios = int(input("Digite o número de pedágios no percurso: ")) #var numero de pedagios recebe valor inteiro por input
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): ")) #var custo pedagio recebe valor float por input do usuario

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia, #chama a função calcular custo viagem
custo_combustivel,
consumo_veiculo, numero_pedagios,

custo_pedagio)

print(f"Custo total da viagem: R${custo_total:.2f}") #mostra o valor total da viagem ao usuario
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}") #mostra o custo total do combustivel da viagem
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}") #mostra o valor total com pedagios da viagem