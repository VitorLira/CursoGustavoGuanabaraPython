# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos, Faça um
# programa que leia o nome dos alunos e mostre a ordem sorteada.

import random

n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quato aluno: ')
lista = [n1, n2, n3, n4]

random.shuffle(lista)
print('A ordem da lista será igual ')
print(lista)
