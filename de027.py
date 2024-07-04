'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e
o último nome separadamente

Ex: Ana Maria de Souza
primeiro: Ana
último: Souza'''
#nomecompleto=str(input('Digite seu nome completo ')).strip()
#nomedividido=nomecompleto.split()
#print('Seu primeiro nome é', nomedividido[0])
#print('já seu último nome é', nomedividido[-1])
nome=str(input('Digite seu nome completo ')).strip().title().split()
print('Seu primeiro nome é', nome[0])
print('já seu último nome é', nome[-1])