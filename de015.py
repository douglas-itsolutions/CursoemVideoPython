# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 0,15 por km rodado
dias=int(input('Quantos dias você ficou com o carro? '))
km=float(input('Quantos kilômetros você percorreu com ele? '))
preço=(60*dias)+(0.15*km)
#print(f'Você terá que pagar R$', preço, 'pelo aluguel')
print('Você ficou {} dias com o carro, rodou {} kilômetros e o custo total do aluguel é de R$ {:.2f})'.format(dias,km,preço))