file = open('poema','a')
file.write("loucaaa")
file.close()
file = open('nota.txt', 'r')
soma = 0
cont = 0
for i in file:
    conv = float(i)
    soma+=conv
    cont+=1

file.close() 

print(soma/cont)   

file = open('poema.txt', 'r', encoding='utf-8')

for l in file:
    if 'mais' in l:
        print(l.strip())

file.close()




