"""
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
    ex: 1843
    unidade: 3
    dezena: 4
    centena: 8
    milhar: 1
"""
# Resolução em str
#
num = int(input('Digite um número entre 0 a 9999: '))
#
# print('unidade', num[3])
# print('dezena', num[2])
# print('centena', num[1])
# print('milhar', num[0])

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
