# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
print(f'O preço {preco} com 5% de desconto ficou {preco - ((preco*5)/100)}')
