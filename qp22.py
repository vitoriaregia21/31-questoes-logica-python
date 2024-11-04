matriz = [[],[],[],[],[]]
soma = 0
for l in range(4):
    for c in range(5):
        matriz[l].append(float(input(f"Digite o que foi vendido no {l+1} trimestre: ")))
print("1- Norte", "2- Nordeste", "3- Sul", "4- Sudeste", "5- Centro-Oeste")
for l in range(4):
    for c in range(5):
        print(f"{matriz[l][c]:^10}", end="")
        soma+= matriz[l][c]
    print()
print("O total foi", soma)
