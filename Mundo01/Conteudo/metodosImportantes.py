"""
Comando 'Type' e metodos de verificação
"""

n = input('Digite algo: ')
# usando o comando 'Type'
print(type(n))  # informa qual o tipo da variável

# usuando os metodos de verificação
print(n.isupper())  # Retorna 'True' se todos os caracteres da string forem maiúsculos;
print(n.islower())  # Retorna 'True' se todos os caracteres da string forem minúsculos;
print(n.isdigit())  # Retorna 'True' se todos os caracteres da string forem digitos;
print(n.isalnum())  # Retorna 'True' se todos os caracteres da string forem alphanumeric, ou sejá, letras e números;
print(n.isalpha())  # Retorna 'True' se todos os caracteres da string forem do alfabeto;
print(n.isdecimal())  # Retorna 'True' se todos os caracteres da string forem decimais;
print(n.isidentifier())  # Retorna 'True' se a string é um identificador;
print(n.isnumeric())  # Retorna 'True' se todos os caracteres na string são numéricos;
print(n.istitle())  # Retorna 'True' se a string segue as regras de um titulo, ou sejá, primeiras letras maiúsculas;
print(n.isprintable())  # Retorna 'True' se todos os caracteres na string são imprimíveis;
print(n.isspace())  # Retorna 'True' se todos os caracteres na string são espaços em branco.
