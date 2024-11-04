#Faça uma função que dada uma frase, retorne o número de palavras
#da frase.

def quant (frase):
    frase = frase.replace(" ", "")
    total = len(frase)
    return total

fra = input("digite: ")
print(quant(fra))

def reverse (numero):
    converte = str(numero)
    converte = converte[::-1]
    return converte


n = int(input("digite o numero:"))
print(reverse(n))

def media (nota1,nota2):
    media = (nota1+nota2)/2
    return media

def status (media):
    if media > 6:
        sta = ("aprovado")
    elif media >=4 and media <= 6:
        sta = ("suplementar")
    else:
        sta = ("REPROVADO")
    return sta

n1= float(input("digite"))
n2= float(input("digite"))
valor = media(n1,n2)
print('média é:', valor )
print('você está', status(valor))
