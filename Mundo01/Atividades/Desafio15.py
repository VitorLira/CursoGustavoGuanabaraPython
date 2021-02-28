#Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais
# quais ele foi lugado. Calcule o proço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Digite a quantidade de dias alugado: '))
km = float(input('Digite a quantidade de Km rodados: '))
print(f'O valor a pagar é = R$ {(dias*60)+(km*0.15):.2f}')
