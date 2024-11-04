tabela=[[],[],[]]
somai = 0
somac1 = 0

for l in range(3):
    for c in range(3):
        tabela[l].append(int(input("Digite o valor:")))

for l in range(3):
    for c in range(3):
        print(f"{tabela[l][c]:^3}", end="")
    print()

for l in range(3):
    for c in range(3):
        if tabela[l][c] % 2 != 0:
            somai+=tabela[l][c]

print("Soma dos números ímpares são: ",somai)

for l in range(3):
    for c in range(1):
        somac1+= tabela[l][c]

menorv = min(tabela[2])

print("soma da primeira coluna é: ",somac1)
print("o menor valor da terceira linha é: ", menorv)

