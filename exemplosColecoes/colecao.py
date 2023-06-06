# Listas 

numeros = [1, 10, 100, 1000]
print(numeros)

# Imprimir o elemento de indice 2, sendo que se inicia no 0
print(numeros[2])

# Operacoes de Listas

# Inclusão de 2 itens usando +=
numeros += [10000, 100000]
print(numeros)

# Substituir os itens nas posições 1 e 2 por 7
# [indice_ incluído: indice_excluido]
numeros[1:3] = [7]
print(numeros)

# Incluir um item na lista usando append 

#O append insere um registro após o último elemento, 
# ou seja, ele é útil quando 
# é preciso colocar o novo registro na última posição da tabela.
numeros.append(1000000000)
print(numeros)

# remover os itens nas posições 1 e 2 da lista
numeros[1:3] = []
print(numeros)

# tamanho da lista
print(len(numeros))