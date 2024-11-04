
#Desenvolva um programa que possa receber o nome e as curtidas das três últimas
#fotos do Instagram de 5 usuários e armazenar tais valores em um dicionário, onde
#a chave é o nome do usuário, e os valores são as curtidas de cada foto. Ao final,
#deverá ser mostrado a média das curtidas de cada usuário (com duas casas
#decimais) e o nome do usuário (com a primeira letra maiúscula) que obteve a
#maior média. Além disso, trate possíveis exceções.

dic = {}
maior = 0
try:
    for i in range(5):
        chave = input("Digite seu nome:").title()
        primeiraf = int(input("quantidade de curtidas:"))
        segundaf = int(input("quantidade de curtidas:"))
        terceiraf = int(input("quantidade de curtidas:"))
        soma = (primeiraf+segundaf+terceiraf)/3
        dic [chave] = soma

except ValueError:
        print('rode o programa novamente')


for chave, valor in dic.items():
        if valor > 0:
            maior=valor
            nome = chave

print(dic)
print(nome, maior)