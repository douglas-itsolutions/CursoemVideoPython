#Escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1=float(input('Digite em centímetros o comprimento da primeira reta: '))
r2=float(input('Digite em centímetros o comprimento da segunda reta: '))
r3=float(input('Agora, da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível formar um triângulo com estas medidas')
else:
    print('Não é possível formar um triângulo com estas medidas')
