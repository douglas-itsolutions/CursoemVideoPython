#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste angulo
#Imagine um circulo, o eixo vertical é o seno, o horizontal é o coseno e vc tem as projeções
# (ex: 45 graus, a em pé é seno e a deitado é coseno
import math
ângulo=float(input('Digite um ângulo '))
radiano=math.radians(ângulo)
coseno= math.cos(radiano)
#seno=math.sin(radiano)
seno=math.sin(math.radians(ângulo))
tangente=math.tan(radiano)
print(f'Para o ângulo de {ângulo:.2f} graus seu radiano é {radiano:.2f}, seu coseno é {coseno:.2f}, o seno é {seno:.2f} e finalmente \n sua tangente é {tangente:.2f}')