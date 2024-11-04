#Faça um programa que peça ao usuário um número inteiro. Em seguida
#mostre na tela os números de 0 a n (número escolhido) e seus respectivos
#quadrados, como na seguinte forma {n : n*n}.
#num = int(input("digite:"))

for i in range (num+1):
    dic[i] = i*3
print(dic)
dic = {'maria':10, 'joao':20, 'pedro':30}
print(dic.fromkeys(['maria', 'joao'],20))

print(dic.fromkeys(['maria','joao'],50))

print(dic.pop('maria'))
print(dic)


n = int(input("digite:"))
dic = {}

for i in range(n+1):
    dic [i] = i*i

del dic[4]

print(dic)
print(len(dic))
dic = {'maria':10, 'joao':50, 'pedro':130}
lista = []
maior = 0
for i in dic.values():
    v = lista.append(i)

print(lista)

for i in lista:
    if i > maior:
        maior = i

print(maior)
men = min(lista)
print(men)
print(max(lista))