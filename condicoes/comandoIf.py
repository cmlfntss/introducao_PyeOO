nome = "Ana"
idade = 25

# comando if (condição se)

if nome == "Ana":
    print("Passou") #condição verdadeira

    if nome == "Ana" or idade == 17 : # Condição V ou V = V
        print("Passou de novo")
        print("%s tem %d anos" %(nome, idade))