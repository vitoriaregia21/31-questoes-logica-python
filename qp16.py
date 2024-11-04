from datetime import date
ano_atual = date.today().year
contmenor = 0
contmaior = 0
for i in range(5):
    nasceu = int(input("Digite o ano que nasceu:"))
    idade = ano_atual - nasceu 
    if idade < 18 :
        contmenor+=1
    else:
        contmaior+=1

print(f"A quantidade de maior de idade são: {contmaior}")
print(f"A quantidade de menor de idade são: {contmenor}")
