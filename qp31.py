#1. Desenvolva um programa que possua um vetor de 10 números inteiros. Após o
#usuário inserir os valores, mostre quantos desses números são maiores, menores e
#iguais ao primeiro elemento do vetor. Além disso, para essa questão trate possíveis
#exceções que poderão surgir.
lista =[]
menor = 0
for i in range(10):
    n =  int(input("Digite o número: "))
    lista.append(n)

menores = 0
maiores = 0
iguais = 0

for i in range(1,10):
    if i[0] < lista[i]:
        maiores += 1
    elif i[0] >lista[i]:
        menores += 1
    else:
        iguais += 1

for i in range (1,10):
        if lista[0] == lista[i]:
            iguais+=1
        elif lista[0] > lista[i]:
            menores+=1
        else:
            maiores+=1         


print("maiores : ", maiores)
print("menores : ", menores)
print("iguais : ", iguais)