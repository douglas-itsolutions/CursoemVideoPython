#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salário=float(input('Digite o seu salário: R$ '))
aumento=salário*(15/100)
final=salário+aumento
#print(f'Seu salário atual é de R$ {salário} e com aumento de 15% ficará R$', salário+aumento)
print('Seu salário atual é de R$ {:.2f} e com aumento de 15% (equivalente a R$ {:.2f}) ele ficará R$ {:.2f}.'.format(salário,aumento,final))