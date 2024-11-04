num1 = int(input("Digite num1: "))
num2 = int(input("Digite o num2: "))
soma = num1 + num2

if soma > 10:
   print(soma+5)
else:
   print(soma-5)
vol = int(input("Digite level do voltor: "))
if vol >= 1 and vol <= 20:
   print (20 + (vol**3))
elif vol > 20 and vol <= 40:
   print(8000+ ((vol-10)**2))
elif vol > 40 and vol <= 60:
    print(9000+(5*vol))
elif vol > 60 and vol <= 80:
   print(9300+(2*vol))
elif vol > 80 and vol <= 100:
   print(9500+vol)
else:
    print("Digite um valor entre 1 e 100")

