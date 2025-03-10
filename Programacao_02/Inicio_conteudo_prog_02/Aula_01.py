class Pessoa: 
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome 
        self.idade = idade


if __name__ == '__main__':
    p1 = Pessoa("Pedro", "Costa", "24") 
    p1.nome = "Teco"
    p1.sobrenome = "Zeira"
    p1.idade = "78"
    print(p1.nome,p1.sobrenome,p1.idade)


    p2 = Pessoa("Kenig", "lol", "24")
    p2.nome = "Kenig"
    p2.sobrenome = "lol"
    p2.idade = "24"
    print(p2.nome,p2.sobrenome,p2.idade)


    p3 = Pessoa("Mairy", "lol", "24")
    p3.nome = "Mairy"
    p3.sobrenome = "lol"
    p3.idade = "24"
    print(p3.nome,p3.sobrenome,p3.idade)

