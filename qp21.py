#Aline está precisando de sua ajuda para poder passar na cadeira de
#álgebra linear. Ela está pedindo para você desenvolver um programa
#que recebe uma matriz 3x3 e retorne:
#
#a) o produto dos elementos da diagonal principal ok
#(valores em vermelho);
#a) a média de todos os elementos da matriz; ok
#b) o maior valor lido da segunda coluna; ok
#c) e exibir na tela os valores menores ou iguais a média. ok

matriz = [[],[],[]]
soma=0

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input("Digite a nota: ")))

for l in range(3):
    for c in range(3):
        soma+= matriz[l][c]

print("a média é:", soma/9)

print("Esses são os valores menor ou igual a média:")
for l in range(3):
    for c in range(3):
        if matriz[l][c] <= soma/9:
            print(matriz[l][c])

somadiag = matriz[0][0]*matriz[1][1]*matriz[2][2]

print("soma da diagonal é: ", somadiag)


if matriz[0][1] > matriz[1][1] and matriz[2][1]:
    maiorv= (matriz[0][1])
if matriz[1][1] > matriz[0][1] and matriz[2][1]:
    maiorv=(matriz[1][1])
if matriz[2][1] > matriz[1][1] and matriz[0][1]:
    maiorv= (matriz[2][1])

print("O maior valor da segunda coluna é: ", maiorv)