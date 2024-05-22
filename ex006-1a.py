n1=int(input('Digite um número :'))
n2=int(input('Digite outro número :'))
som=n1+n2
sub=n1-n2
div=n1/n2
din=n1//n2
res=n1%n2
mul=n1*n2

#print(f'A soma é {som}, a subtração é {sub}, a divisão normal é {:div .3f}')
#A divisão fica com 03 casas flutuantes
print('A soma é {}, a subtração é {} e a divisão normal é {:.3f} :'.format (som, sub, div))
#print(f'A divisão inteira é {din}, o resto da divisão é {res} e a multiplicação é {mul}')