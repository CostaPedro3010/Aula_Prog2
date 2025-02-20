Lista = []
dicionario = {}

print(type(dicionario))

dicionario['Porto Alegre'] = 1500000
dicionario['Alegrete'] = 75000
dicionario['Pelotas'] = 340000
dicionario['Caxias'] = 480000
dicionario['Canoas'] = 360000
dicionario['Gravatai'] = 280000
dicionario['Cachoeirinha'] = 140000
dicionario['Guaiba'] = 95000
dicionario['Santa Maria'] = 280000
dicionario['Gramado'] = 70000
dicionario['Canela'] = 70000

chaves = dicionario.keys()

for k in chaves:
    print(k, dicionario[k])

print("-----------------Como ordenar por valor----------------------")
print("---------------teste 01--------------------------")
for cidades in dicionario:
    print(cidades, dicionario[cidades])    

dicionario_ordenado = sorted(dicionario.values(), reverse=True)
print(dicionario_ordenado)


print("--------------------copia do colega-------------------")

for i in sorted(dicionario.values(), reverse=True):
    print(i)



print("--------------------explicação iuri-------------------")

#print(dicionario.items())
x = dicionario.items()

x = sorted(x, key=lambda item: item[1])
print(x)
