with open("animais.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    
for linha in linhas:

    animal = linha.strip()
    print(f"Animal: {animal}")