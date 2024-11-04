anoadm = int(input("Digite o ano de admissão: "))
salarioatual = float(input("Digite seu salário: "))
ultimoreaj = int(input("Ano do último reajuste? "))

quant = 2023 - ultimoreaj

tempo = 2023 - anoadm

if quant >= 2 and tempo > 10 :
    porcentagem = salarioatual*0.30
    print(salarioatual+porcentagem)
elif quant >= 2 and tempo >= 5:
    porcentagem = salarioatual*0.20
    print(salarioatual+porcentagem)
elif quant >= 2 and tempo < 5:
    porcentagem = salarioatual*0.10
    print(salarioatual+porcentagem)
else:
    print("Você não está apto a receber")