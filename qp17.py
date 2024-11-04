n = int(input("Digite o número:"))
ac = 0
for i in range(1,n):
    if n % i == 0:
        ac+=i
if ac == n:
    print(f"{n} é um número perfeito")
else:
    print(f"{n} não é um número perfeito")
for i in range(5,100):
    if i % 7 == 0:
        if not i % 5 == 0:
            print(i)




