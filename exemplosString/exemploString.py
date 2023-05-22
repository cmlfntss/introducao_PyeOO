# Concatenação 

programacao = "Programação" #pode ser delimitado por aspas simples
#ou duplas
oo = 'OO' #.. o melhor é usar o mesmo padrão de aspas

programacao_oo = programacao + " " + oo
print(programacao_oo)

# Tamanho 

print(len(programacao_oo)) #len serve para 'mostrar' número de itens 
#em um determinado objeto

# Indexação e substrings

frase = "Python é muito divertido!"

# A indexação começa com 0

print(frase[3])

# use -1 para pegar a última letra

print(frase[-1])

# -2 use para pegar a penúltima letra

print(frase[-2])

# string[start:end] - end não é incluso
print(frase[:4]) #pega as quatro primeiras letras
print(frase[10:]) #pega as dez últimas ignorando as primeiras
print(frase[5:10]) #pega a 5 letra e a 10
print(frase[:]) #pega a frase completa

# Multiplicação de strings por um número


ola = "olá"
sete_olas = ola * 7
print(sete_olas)
#imprime sete vezes a variavel olá

# Operador In

programacao_python = "Programação em Python"

# checa se a string contém "Python"
print("Python" in programacao_python)

# checa se a string contém "python"
print("python" in programacao_python)

# checa se a string contém "abacate"
print("abacate" in programacao_python)
#Sempre retornando nas verificações/prints os valores true or false

# Escaping

print("Eu estou estudando\n" + programacao_python) #adiciona uma nova linha quando
#incluímos \n


# Maiúsculas e Minúsculas

print(programacao_python.lower()) #todas minúsculas
print(programacao_python.upper()) #todas maiúsculas

tudo_minuscula = "aula de python com a professora Tatiana"
print(tudo_minuscula.capitalize()) #faz com que apenas a primeira letra seja maiúscula

# Formatação

nome = "Camila"
numero_inteiro = 29
numero_decimal = 5.3321

print("Olá, meu nome é %s! Tenho %d anos e %d reais de salário"
  %(nome, numero_inteiro, numero_decimal)) #float impresso como int

print("Olá, meu nome é %s! Tenho %d anos e %f reais" 
      % (nome, numero_inteiro, numero_decimal)) #float impresso como float

print("Olá, meu nome é %s! Tenho %d anos e %.2f"
      %(nome, numero_inteiro, numero_decimal)) #float impresso como float com duas casas decimais

