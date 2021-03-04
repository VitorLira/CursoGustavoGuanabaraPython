#Crie um programa que leia um número Real qualquer e mostre na tela a sua porção inteira. ex 6.127 -> 6

from math import trunc

num = float(input('Digite um numero real para saber a sua porção inteira: '))
print('A porção inteira do número {}, é = {} '.format(num, trunc(num)))

# outro modo de fazer resolver

print('A porção inteira do número {}, é = {} '.format(num, int(num)))
