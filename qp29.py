#Deverá ser criado um arquivo .txt o qual irá conter seus dados
#pessoais (nome completo, profissão, graduação, faculdade....).
#Na sequência, o arquivo deverá ser lido e as seguintes informações
#exibidas:
#
#a) Exibir todos os dados;
#b) Quantidade de palavras;
#c) Quantidade de caracteres.

file = open('dados.txt', 'r', encoding='utf8')

print(file.read())
file.seek(0)

quant = []
contp = 0
quantcara = []
quantc = 0

for i in file.readlines():
    adicionar = quant.append(i)
    
for i in quant:
    j = i.split()
    for p in j:
        contp+=1
        for k in p:
            adc = quantcara.append(k)

for h in quantcara:
    quantc+=1
  
file.close()

print("quantidade de palavras: ",contp-1)
print("quantidade de caracteres: ",quantc)