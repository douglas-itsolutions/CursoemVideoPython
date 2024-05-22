#Escreva um programa que leia um ano e mostre se ele é bissexto
'''ano=int(input('Digite um ano: '))
if ano%4==0 and ano%100!=0 and ano%400==0:
    print('Trata-se de um ano bissexto')
else:
    print('Não é um ano bissexto')'''
from datetime import date
ano=int(input('Que ano você quer analisar? Caso queira o atual, digite 0 '))
if ano==0:
    ano=date.today().year
    print(f'O ano atual é {ano}')
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('Trata-se de um ano bissexto')
else:
    print('Não é um ano bissexto')