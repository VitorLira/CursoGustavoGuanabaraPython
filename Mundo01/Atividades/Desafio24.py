"""
    Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
"""
cidade = str.strip(input('Digite o nome da cidade: '))
cidade = cidade.title().split()
print('esta cidade começa com o nome "Santo"? ', 'Santo' in cidade[0])

