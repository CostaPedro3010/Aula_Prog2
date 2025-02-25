def soma2(x1, x2):
    soma = x1 + x2
    return soma

soma = soma2(2,2)#4
print(soma)

def sub2(x1, x2):
    sub = x1 - x2
    print(sub)
sub2(10,4) #6
print(sub2(10,3)) #none



def mult2():
    print("Operacao de multiplicacao")
    x1 = input("insira o primeiro valor: ")
    x2 = input("insira o segundo valor: ")
    return (int(x1)*int(x2))

print(mult2())


def podeBeber(idade):
    if (idade>= 18):
        return True
    else:
        return False
    

idade = 4
if podeBeber(idade):
    print("pode beber")
else:
    print("não pode beber :()")

def recebe_tres_valores(x1, x2, OP):
    if OP == "mult":
        resultado = x1 * x2
    elif OP == "sub":
        resultado = x1 - x2
    elif OP == "soma":
        resultado = x1 + x2
    elif OP == "div": 
        resultado = x1 / x2
    else:
        print("vc digitou uma operacao invalida")
    return resultado

valor1 = int(input("Informe o primeiro Valor: "))
valor2 = int(input("Informe o primeiro Valor: "))
tipoOP = input("Informe Qual tipo de operação: ")
print("O Resultado da Operacao foi: ",recebe_tres_valores(valor1,valor2,tipoOP))

def soma_lista(lista):
    soma = 0
    for x in lista:
        soma = soma + x 
    return soma

print("O resultado da soma da lista foi:",soma_lista([1,2,3,4,5,6]))
print("O Resultado da Operacao foi: ",recebe_tres_valores(OP='soma', x1= 8, x2= 5))
