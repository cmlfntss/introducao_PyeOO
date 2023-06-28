class Calculadora:
    def __init__(self):
       self.valor_interno = 5

    def adiciona(self, numero):
        # não podemos chamar a variável valor interno sem self, pq 'valor' é
        # um atributo de calculadora

        return self.valor_interno + numero
total = Calculadora()
print("O resultado é = %d" % total.adiciona(3)) #self pegará o valor de 5 de valor interno e o valor irá pegar 3 para número