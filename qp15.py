while valor!=0 :
    if valor < 0 :
        print("valor não pode ser adicionado")
    else:
        soma+=valor
    valor = float(input("Digite o valor: "))
        
    
if soma > 1000:
    soma = soma - (soma * 0.10)
   
print(soma)



