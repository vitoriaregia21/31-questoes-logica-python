for i in range(1,5):
    for k in range(1,5):
        print(i*k, end=" ")
    print()

idade = [7,10,15,18,23]
idade.remove(7)
idade.append(41)
idade.insert(2, 19)
idade.sort(reverse=True)
idade.remove(10)
idade.pop()
idade.pop(0)
idade[0]= 17
idade [1] = 18
idade [2]= 19
quant = len(idade)
print(idade)
print(quant)

nomes = []

nomes.append("maria")
nomes.append("julia")
nomes.append("miguel")
for i,n in enumerate(nomes):
    print(f"indice {i} e nome {n}")


lista = []

for i in range(5):
    valor = int(input("Digite:"))
    lista.append(valor)
print(lista)

valores = [3.5, 6.7, 1.0, 4.90]

valores.insert(1, 2.3)
valores.pop()
valores[2] = 9.2
valores.sort()
quant = len(valores)
print("quantidade de valor da lista: ",quant)

for i, j in enumerate(valores):
    print(f"indice {i}, e valor {j}")

nome = ["kai", "fe", "vi", "ma", "ju", "mi"]
idade = [2,5,7,10,15,20]

juntar = nome+idade

print(juntar)

compras = [7.0, 10.0, 30.0, 50.0, 7.0, 3.0]

print(f"A compra mais cara foi {max(compras)}")
print(f"A compra mais barata foi {min(compras)}")
print(f"O total de compras foi {sum(compras)}")
print(f"o total dividido pela quantidade de intens é: {sum(compras)/len(compras)}")
print(compras.count(7.0))
print(compras.index(10.0))



lista= []

for i in range(5):
    n1 = float(input("n1:"))
    n2 = float(input("n2:"))
    media = (n1 + n2)/2
    lista.append(media)

soma = sum(lista)
mediaturma = soma/len(lista)

print("A média da turma é:",(mediaturma))
for i in lista:
    if i > mediaturma:
        print("as notas superiores a media da turma é:",i)

