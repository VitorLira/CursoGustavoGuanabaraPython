# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e
# mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o cateto oposto da hipotenusa: '))
ca = float(input('Digite o cateto adjacente da hipotenusa: '))
hi = hypot(co, ca)
print('A hipotenusa do triangulo é = {:.2f}'.format(hi))
co1 = float(input('Digite o cateto oposto da hipotenusa: '))
ca1 = float(input('Digite o cateto adjacente da hipotenusa: '))
hi1 = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é igual a {:.2f}'.format(hi1))
