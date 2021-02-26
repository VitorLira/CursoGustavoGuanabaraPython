# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite o valor que você tem em dinheiro: '))
print(f'{real:.2f}R$-BR podem comprar {real/5.53:.2f}$Dólares-EUA')
