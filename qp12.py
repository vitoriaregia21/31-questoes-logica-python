n = input("digite o valor:")
lista = []
cresc = []
for i in n:
    lista.append(int(i))
    cresc.append(int(i))

cresc.sort()

if lista == cresc:
    print('SIM')
else:
    print('NÃO')