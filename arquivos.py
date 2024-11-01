with open("arquivo.txt", "+r") as file:
    leitura = file.read()
    print(leitura)

with open("arquivo.txt", "+w") as file:
    frase = f''' "Melhor é o que tarda em irar-se do que o poderoso, e o que controla o seu ânimo do que aquele que toma uma cidade." (Provérbios 16.32)'''
    file.write(frase)

with open("arquivo.txt", "+r") as file:
    leitura = file.read()
    print(leitura)

with open("arquivo.txt", "+a") as file:
    frase = f''' Só para refletir... '''
    file.write(frase)

with open("arquivo.txt", "+r") as file:
    leitura = file.read()
    print(leitura)