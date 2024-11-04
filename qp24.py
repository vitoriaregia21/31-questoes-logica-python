teste = 'Sorria! Hoje é um dia feliz!'

nova = teste[:12] + " é para ser" +teste[21:]

print(nova)


nome = 'Vitoria'
sobre = 'Regia'

print(nome,sobre)
print(nome,",", sobre)
print(nome + sobre)
print(f'{nome},{sobre}')
print('{},{}'.format(nome,sobre))
frase = 'feliz aniversário, pessoa'
mude = frase.replace('pessoa', 'MIGUEL')

print(mude.count('I'))
print(mude.capitalize())
print(mude.title())
print(mude.upper())
print(mude.lower())
print( mude.split())
print(mude.strip())
print(" - ".join(mude))
nome = input("Digite seu nome:")

novo = nome.split()
print(novo)
print("-".join(novo))