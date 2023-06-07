print("***************************************************")
print("O aluno foi aprovado?")
print("***************************************************")

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))

media = (nota_1 + nota_2 + nota_3)/3

if media >= 7:
    print("Aluno APROVADO! A sua média foi %.2f" % media)
elif media < 3:
    print("O aluno foi REPROVADO! A sua média foi %.2f" % media)
else: 
    print("O aluno está de PROVA FINAL! A sua média foi %.2f" % media)