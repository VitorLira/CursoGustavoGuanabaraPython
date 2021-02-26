# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%.

salario = float(input('Digite o seu salário: '))
print(f'O seu salário de {salario:.2f}R$, recebeu um aumento de 15% e ficou {salario + ((salario*15)/100):.2f}R$')
