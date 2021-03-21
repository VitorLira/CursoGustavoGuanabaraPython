"""

Formas de fatiamento

    frase[início:fim:salto]
    frase[:fim] -> vai do início da string ate o índice anterior informado após os dois pontos ':'
    frase[início:] -> vai do índice informado até o final da string
    frase[início::2] -> vai do índice inicial informado ate o final da string pulando de 2 em 2 casas de índices.

Analise de strings

    frase.len() <- informa quantos caracteres tem uma string.

    frase.count('letra') <- irá retornar o número de vezes que a letra passada como parametro foi encontrada na frase.
    - obs: o frase.count('letra') pode ser feito fatiamento em conjunto, ex: frase.count('letra':início:fim)

    frase.find('palavra') <- irá retornar a posição do índice onde a palavra começa /
    - obs: no frase.find('palavra') se for passado uma palavra que não existe, o mesmo irá retornar ' -1 '

    'palava' in frase <- irá retorna 'True' ou 'False' caso exista ou não

Transformação

    frase.replace('palavra1', 'palavra2') <- ela irá procurar a palavra1 dentro da frase, e sempre que encontrar irá
    substituir pela palavra2, somente na mostragem a frase na tela, para alterar diretamente dentro da variável 'frase'
    tem que ser escrita desta forma -> frase = frase.replace('palavra1', 'palavra2')

    frase.upper() <- irá transformar todas as letras da frase para maiúsculas

    frase.lower() <- irá transformar todas as letras da frase para minpusculas

    frase.capitalize() <- irá colocar a primeira letra da frase para maiúsculo e todo o resto para minúsculo.

    frase.title() <- irá verificar toda a frase, e irá colocar a primeira letra e todas as letras após espaços
    para maiúsculo. ex: curso em vídeo -> Curso Em Vídeo

    frase.strip() <- irá remover os espaços inúteis que estiverem antes e após a frase

    frase.rstrip() <- irá remover apenas os espaços inúteis que estaram ao fim da string (ao lado direito) r > right

    frase.lstrip() <- irá remover apenas os espaços inúteis que estaram ao início da string (a esquerda) l > left

Divisão

    frase.split() <- irá dividir a string onde estiver espaços; formando varias strings, cada uma com um índice
    ou seja, irá criar uma lista apartir de um conjunto de caracteres.

Junção

    'simbolo'.join(frase) <- ira unir todos os índice de uma lista pelo símbolo ou espaço entre as aspas simples
    tornando a lista um conjunto de caracteres unico.

"""
