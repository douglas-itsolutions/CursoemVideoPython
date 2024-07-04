'''Faça um programa que leia uma frase pelo teclado, digitada pelo usuário e mostre:

- Quantas vezes aparece a letra A
- Em qual posição ela aparece a 1a. vez
- Em qual posição ela aparece a última vez'''
#frase=str(input('Digite uma frase ')).strip()
#fraselower=frase.lower()
#print('Quantas vezes aparece o caracter "a" em sua frase?', fraselower.count('a'), 'vezes')
#print('O caracter "a" aparece pela 1a. vez na posição ', fraselower.find('a'))
#print('e aparece na última posição ', fraselower.rfind('a'))'''
frase=str(input('Digite uma frase ')).strip().upper()
print('Quantas vezes aparece o caracter "a" em sua frase?', frase.count('A'), 'vezes')
print('O caracter "a" aparece pela 1a. vez na posição ', frase.find('A')+1)
print('e aparece na última posição ', frase.rfind('A')+1)