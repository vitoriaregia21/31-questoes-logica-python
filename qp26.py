#Faça um programa que pergunte para um gerente de uma lanchonete se ele
#deseja remover, adicionar ou modificar o valor de um produto do cardápio,
#apenas encerrando o algoritmo quando o usuário decidir. No final, mostre o
#cardápio com as modificações. Segue o cardápio original (já cria o dicionário
#com esses valores):

menu = {'coxinha':5.00, 'pastel': 4.00, 'suco':3.00,'bolo':4.50}
lista = ['adicionar','remover', 'modificar']
print(menu)
deseja = input('deseja remover, adicionar ou modificar o valor de um produto do cardápio:').lower()

while deseja == lista[0] or lista[1] or lista[2]:
    if deseja == 'adicionar':
        adicionar = input("nome do item: ")
        valor = float(input("valor:"))
        menu[adicionar] = valor
        
    if deseja == 'remover':
        item = input('nome:')
        if menu.get(item):
            menu.pop(item)
           
    if deseja == 'modificar':
        item  = input("nome do item: ")
        novov = float(input("valor:"))
        if menu.get(item):
            menu[item] = novov
           
    deseja = input('deseja remover, adicionar ou modificar o valor de um produto do cardápio:').lower()        
tupla = ('santa','maringa', 'náutico', 'bahia', 'ibis','sao paulo','flamengo','palmeiras','santos','portelinha ')

print(tupla[0:5])
print(tupla[6:10])

for i in sorted(tupla):
    print(i)

for i in tupla:
    if i == 'sao paulo':
        print(len(i)+1)

 
