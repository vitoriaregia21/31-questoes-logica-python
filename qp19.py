saltos = []
cont= 0
nome = input("Digite seu nome:").lower()

while nome != "sair":
    for i in range(5):
        salto = float(input("Digite o tamanho do seu salto: "))
        saltos.append(salto)        
    print("**** RESULTADO ****")
    print(f"Atleta: {nome}")
    for k  in (saltos):
        cont+=1
        print(f"{cont}º Salto: {k}") 
    print("A média dos saltos é: ", sum(saltos)/5)


matriz = [[],[]]

for l in range(2):
    for c in range(4):
        matriz[l].append(int(input("Digite o valor:")))

for l in range(2):
    for c in range(4):
        print(f"{matriz[l][c]:^4}", end="")
    print()