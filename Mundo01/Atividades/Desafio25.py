'''
    Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no mome.
'''

nome = str.strip(input('Digite seu nome completo: '))
print('o nome "Silva" esta no seu nome? ', 'silva' in nome.lower())
