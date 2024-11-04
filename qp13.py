num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o último número"))
somapares = 0

while num1 <= num2:
    if num1%2==0:
        somapares+=num1
    num1+=1

print("A soma dos pares:", somapares)
valor = float(input("Digite o valor: "))
soma = 0
