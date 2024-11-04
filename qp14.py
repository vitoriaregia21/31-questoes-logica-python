nota = 0
cont = 0
soma = 0

while nota != -1:
    nota = int(input("Digite a nota:"))
    if nota == -1:
        print("programa encerrado")
    else:
        soma+=nota
        cont+=1
print(f"A quantidade de notas {cont}")
print(f"A média é: {soma/cont:.2f}")