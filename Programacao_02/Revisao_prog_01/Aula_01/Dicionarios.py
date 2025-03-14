dicionario = {
    'Porto Alegre' : 1500000,
    'Alegrete':  75000,
    'Pelotas': 340000,
    'Caxias': 480000,
    'Canoas': 360000,
    'Gravatai': 280000,
    'Cachoeirinha': 140000,
    'Guaiba': 95000,
    'Santa Maria': 280000,
    'Gramado': 70000,
    'Canela': 70000
}

print("-----------------Como Mostar cidade e Valores----------------------")
chaves = dicionario.keys()
for k in chaves:
    print(k, dicionario[k])

print("-----------------Como Mostar cidade e Valores de outra maneira para não usar apenas uma letra----------------------")
for cidades in dicionario:
    print(cidades, dicionario[cidades])   

print("-----------------Como ordenar por valor----------------------")
dicionario_ordenado = sorted(dicionario.values(), reverse=True)
print(dicionario_ordenado)

print("--------------------explicação iuri-------------------")
x = dicionario.items()
x = sorted(x, key=lambda item: item[1])
print(x)
