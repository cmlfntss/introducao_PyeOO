# Funções

# definir uma função chamada hello_world

def hello_world():
    print("Hello, World!")
    print("Oi, Mundo!")
    print("Salut, Monde!")
    print("Hola, Mundo!")

    # chamar a função 3 vezes

    for i in range(3):
        hello_world()


#funções com parâmetros

# x é um parâmtro

def uma_funcao(x):
    print("x = %d" % x)

# passar 5 para uma função
# aqui, 5 é um argumento passado para a função

uma_funcao(5)


# funções com retorno

# função que retorna a soma de dois números

def soma (a, b):
    return a + b

c = soma(7, 5)
print("c = %d" % c)

# funções com parâmetros default

# funções com parâmetros default (padrão)

def multiplica (a, b=2):
    return a * b
print(multiplica(5, 84))

# como b tem um valor padrão, podemos passar apenas um argumento

print(multiplica(7))