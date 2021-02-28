# escreva um programa que converta um temperatura digitada em °C e converta par °F.

graus = float(input('Digite a temperatura em °C : '))
print(f'A temperatura {graus:.2f}°C é igual a {(graus*9/5)+32:.2f}°F = Fahrenheit')
