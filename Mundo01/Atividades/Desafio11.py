# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m² .

alt = float(input('Digite a altura em metros: '))
lar = float(input('Digite a largura em metros: '))
print(f'A area a ser pintada é igual a {alt*lar:.2f}m², vamos precisar de {(alt*lar)/2**2:.2f} litro de tinta.')
