"""
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras em maiúsculas;
    - O nome com todas as letras em minúsculas;
    - Quantas letras ao todo (sem considerar espaços);
    - Quantas letras tem o primeiro nome.
"""

nome = str.strip(input('Digite o seu nome completo: '))

print(nome.upper())
print(nome.lower())
nome = nome.split()
nome1 = ''.join(nome)
print(len(nome1))
print(len(nome[0]))
