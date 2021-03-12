# Um professor quer sortear um dos seus quatros alunos para apagar o quadro, Faça um programa que ajude ele ,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
sorteio = [nome1, nome2, nome3, nome4]
escolhido = choice(sorteio)

print('O escolhido foi -', escolhido)
