"""
    Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
    aparece a primeira vez e em que possição ela aprarece a última vez.
"""

frase = str.strip(input('Escreva uma frase: '))
print('A letra "a" apareceu {} vezes na frase.'.format(frase.lower().count('a')))
print('A primeira vez que a letra "a" aparece e no indice {}.'.format(frase.lower().find('a')))
print('A ultima vez que a letra "a" aparece e no indice {}.'.format(frase.lower().rfind('a')))
