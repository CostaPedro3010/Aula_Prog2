class Pessoa: 
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome 
        self.idade = idade
    
    def exibir(self):
        print(f"{self.nome} {self.sobrenome} {self.idade}")


if __name__ == '__main__':
    p1 = Pessoa("Pedro", "Costa", "24") 
    p2 = Pessoa("Kenig", "lol", "24")
    p3 = Pessoa("Mairy", "lol", "24")
    
    lista_Pessoas = [
        Pessoa("Anakin","Skywalker","24"),
        Pessoa("Darth","Vader","42"),
        Pessoa("Minch","Yoda","1000"),
        Pessoa("Luke","Skywalker","62") 
    ]

    lista_Pessoas.append(p1)
    lista_Pessoas.append(p2)
    lista_Pessoas.append(p3)

    for pessoas in lista_Pessoas:
        pessoas.exibir()