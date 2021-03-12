# Faça um programa que leia um ãngulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math
angulo = float(input('Digite o valor do angulo para saber o seno, cosseno e tangente: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Os valores do angulo {}° são: cosseno = {:.2f}, seno = {:.2f}, tangente = {:.2f}'.format(angulo, seno, cosseno, tangente))
