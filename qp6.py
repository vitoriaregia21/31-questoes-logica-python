v = int(input("Digite 0 ou 1 para vascularização:"))
s = int(input("Digite 0 ou 1 para sementes:"))
f = int(input("Digite 0 ou 1 para flores:"))


if v == 0 and s == 0 and f == 0:
   print("Briófita")
elif v == 1 and s == 0 and f==0:
   print("Pteridófita")
elif v == 1 and s ==1 and f==0:
    print("Gminosperma")
elif v == 1 and s ==1 and f==1:
   print("Angiosperma")
else:
   print("não existe essa opção")