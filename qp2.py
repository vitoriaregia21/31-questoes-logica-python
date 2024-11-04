quantcarros = int(input("Digite a quantidade de carros: "))
valortotalv = float(input("total de vendas?"))
salariofixo = float(input("Digite o valor do seu salário: "))
valorporcarro = float(input("Digite o valor que recebe por carro vendido: "))

total = salariofixo + (quantcarros * valorporcarro) + (valortotalv* 0.05)
print(f"Salário total:{total:.2f}")