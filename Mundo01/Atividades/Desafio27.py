"""
    Faça um programa que leia o nome completo de uma pessoa,
    mostrando em seguida o primeiro e o último nome separadamente.
"""
nome = str.strip(input('Digite seu nome copleto: ')).split()
print('Seu primeíro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[-1]))
