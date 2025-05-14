import random

with open ("animais.txt","r") as ex3:
    linhas = ex3.read().splitlines()

nome_do_animal = random.choice (linhas)

print("Animal sortedado:",nome_do_animal)