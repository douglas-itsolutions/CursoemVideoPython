#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
#Para inferiores ou iguais, o aumento é de 15%
salarioatual = float(input('Digite seu salário em Reais: '))
salariomenor = salarioatual + (salarioatual * 15/100)  #ou (salarioatual * 0.15)
salariomaior = salarioatual + (salarioatual * 10/100)  #ou (salarioatual * 0.10)
if salarioatual <= 1250:
    print('Quem ganhava R$ {:.2f}, com aumento passará a ganhar R$ {:.2f}'.format(salarioatual, salariomenor))
else:
    print('Quem ganhava R$ {:.2f}, com aumento passará a ganhar R$ {:.2f}'.format(salarioatual, salariomaior))