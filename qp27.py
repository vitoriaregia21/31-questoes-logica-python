
#Crie um programa que vai escrever na tela a seguinte String:
#'Python rainha, portugol nadinha'
#
#a) Com todas as letras maiúsculas;
#b) Com todas as letras minúsculas;
#c) Apenas com a primeira letra maiúscula;
#d) A primeira letra de cada palavra maiúscula;
#e) Quantas vezes a letra “a" se repete na string;
#f) Uma nova string na qual a palavra “nadinha” seja trocada por “ ”.
#frase = 'Python rainha, portugol nadinha'

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.count('a'))
nova = frase.replace('nadinha', 'feinha')
print(nova)

print('{0},{1},{2}'.format('a','b','c'))
print('{2},{1},{0}'.format('a','b','c'))
print('{1},{2},{0}'.format('a','b','c'))
valor = int(input("digite:"))
print('{0:b}'.format(valor))
teste = 'Sorria! Hoje é um dia feliz!'
print("-".join(teste))
frase = input("digite:").lower( )

frasesem = frase.replace(" ", "")


if frasesem[::-1] == frasesem:
    print("é um palíndromo")
else:
    print("não é um palíndromo")
dados = {'Miguel': 5,
        'Vanessa': 22,
        'Raiane':33}

print(dados['Miguel'])
print(dados.get('Ray', 'não enc'))

dados['Clau'] = 50

print(dados)


