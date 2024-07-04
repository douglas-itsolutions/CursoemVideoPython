#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o nº escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep #biblioteca para fazer sistema aguardar alguns segundos
chutepc=random.randint(0,5) #faz o computador sortear
chuteusuario=int(input('Entre 0 e 5, qual número o computador escolheu? '))
print('Processando...')
sleep(3) #3segundos de espera
if chuteusuario == chutepc:
    print('Parabéns, Você venceu! o computador também escolheu', chutepc)
else:
    print('Você perdeu, o computador escolheu', chutepc)
