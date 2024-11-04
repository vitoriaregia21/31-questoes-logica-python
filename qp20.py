lista = []
soma = 0
maior = 0
menor = 100000
quant = int(input("quantos produtos você vendeu:"))

for i in range(quant):
    peso = float(input("digite o peso de cada item: "))
    lista.append(peso)
    soma+=peso
    media = soma/quant

    if peso > maior:
        maior = peso
    
    if peso < menor:
        menor = peso

print(f"a média foi {media}")
print(f"menor valor foi {menor}")
print(f"maior valor foi {maior}")
print(f"valor arrecadado foi {soma*4.35}")



                                               
