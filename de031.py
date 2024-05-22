#Escreva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens de até 200Km e R$ 0.45 para
#viagens mais longas
distancia=float(input('Qual a distância da sua viagem em km? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
#print(f'Você está prestes a começar uma viagem de {distancia}km')
if distancia>200:
#    print('O preço da passagem ficará R$', distancia*0.45)
    print('O preço da passagem ficará R$ {:.2f}'.format(distancia*0.45)) #deixa a resposta com 02 casas decimais
else:
    print('O preço da passagem ficará R$ {:.2f}'.format(distancia*0.50))

'''exemplo de codigo em uma linha, if inline, operador ternario ou simplesmente if simplificado: 
preço= distancia * 0.50 if distancia <= 200 else distancia * 0.45
print (preço)'''
