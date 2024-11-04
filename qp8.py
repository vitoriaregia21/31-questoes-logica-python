consumo = int(input("Dgite seu consumo de energia:"))

if consumo <= 500:
    total = (consumo * 0.02) + 5.00
elif consumo > 500 and consumo <= 1000:
    total = (consumo * 10.00) + 5.00
elif consumo > 1000:
    total = (consumo * 35.00) + 5.00


print("seu gasto é de", total)