class Carro:
    
    def __init__(self):
        self.cor = "preto"

# um novo carro é criado com a cor = preto

carro_1 = Carro()
print(carro_1.cor)

#alterando o valor da cor de carro_1 para branco

carro_1.cor = "branco"
print(carro_1.cor)

class Carro2:
    
    def __init__(self, cor):
        self.cor = cor