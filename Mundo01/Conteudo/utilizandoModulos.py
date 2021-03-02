"""
**********************Utilizando Modulos****************************

O modulo 'Math' é para utilizar funções da matemática.
ceil  -> faz o arredondamento de um número para cima.
floor -> faz o arredondamento de um número para baixo.
trunc -> elimina os números após as casas decimais.
pow   -> para utilizar potenciação ex -> pow(2, 3)
sqrt  -> para encontrar a raiz quadrada de um número.
factorial -> para fatorar um numero.
"""
"""
O modulo 'Random' é para gerar um número aleatorio entre 0 e 1. ex print(random.random)
para gerar aleatoriamente um número inteiro se utiliza o 'randint' após o ponto. ex print(random.randint(1, 10)
nesse exemplo é para gerar um número entre 1 a 10.
"""
import math
import random
# Achando a raiz quadrada de um número
num = int(input("Digite um numero para saber a raiz quadrada: "))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, math.ceil(raiz)))  # para arredondar a raiz -> math.ceil(raiz)

# Gerando um número aleatorio
num1 = random.random()
num2 = random.randint(1, 20)
print('Onumero aleatorio entre 0 e 1 foi {:.2f}, e entre 1 e 20 foi {}'.format(num1, num2))
