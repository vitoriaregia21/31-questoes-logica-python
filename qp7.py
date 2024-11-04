idade = int(input("Digite sua idade:"))
if idade < 4 or idade > 60:
   print("Entrada gratuita")
elif idade >=4 and idade < 18:
   print("entrada por 20R$")
else:
    print("entrada por 30R$")