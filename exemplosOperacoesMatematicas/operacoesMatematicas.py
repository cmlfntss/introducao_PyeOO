# Operações Aritméticas

um_inteiro = 7

# Soma, subtração, multiplicação e divisão


resultado_1 = 7 + 5
resultado_2 = um_inteiro - resultado_1
resultado_3 = resultado_2 * 3
resultado_4 = resultado_3 / 4

# imprimindo os resultados concatenando uma string com o resultaod numérico

print("O resultado da soma é = " + str(resultado_1))
print("O resultado da subtração é = " + str(resultado_2))
print("O resultado da multiplicação é = " + str(resultado_3))
print("P resultado da divisão é = " + str(resultado_4))

# imprimindo os resultados de potencialização e resto da divisão

resultado_5 = 2 ** 4
resultado_6 = resultado_5 % 4
resultado_7 = 13 % 4

# imprimindo os resultados da concatenação uma string com os resultados numéricos
print("O resultado da potencialização é = " + str(resultado_5))
print("O resultado do resto da divisão é = " + str(resultado_6))
print("O resultado do resto da divisão é = " + str(resultado_7))

# Incremento e decremento
# decrementando 2 unidades

um_inteiro -= 3
print("O resultado é = " + str(um_inteiro))  # 7 - 3 = 4 agora um inteiro é 4


um_inteiro += 5
print("O resultado do novo incremento com cinco unidades é = " + str(um_inteiro))
