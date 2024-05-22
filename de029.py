#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h mostre uma mensagem que ele foi multado. A multa vai custar R$ 7,00 por cada km acima
#do limite
velocidade=float(input('Qual a velocidade que estava o carro? '))
excesso=(velocidade)-(80)
multa=(excesso)*(7) #ou multa=(velocidade-80)*7
if velocidade >80:
    print('Seu carro será multado em R$ {:.2f} '.format(multa))
else:
    print('Seu carro não será multado')

print('Dirija com segurança, tenha um bom dia!') #este print, colado ao canto sempre será mostrado