class Empresa:
    def __init__(self, nome, endereco, servico):
        self.nome = nome
        self.endereco = endereco
        self.servico = servico

    def exibir_empresa(self):
        print(f"{self.nome} {self.endereco} {self.servico}")

class Remedio:
    def __init__(self, nome, Tarja, Laboratorio):
        self.nome = nome
        self.Tarja = Tarja
        self.Laboratorio = Laboratorio

    def exibir_remedio(self):
        print(f"{self.nome} {self.Tarja} {self.Laboratorio}")

class Funcionario:
    def __init__(self, Nome, Sobrenome, Cargo):
        self.Nome = Nome
        self.Sobrenome = Sobrenome
        self.Cargo = Cargo

    def exibir_funcionario(self):
        print(f"{self.Nome} {self.Sobrenome} {self.Cargo}")

class Livro:
    def __init__(self, Titulo, Autor, Editora):
        self.Titulo = Titulo
        self.Autor = Autor
        self.Editora = Editora

    def exibir_livro(self):
        print(f"{self.Titulo} {self.Autor} {self.Editora}")

if __name__ == '__main__':
    lista_Empresas = [
        Empresa("Jedi", "Ahch-to", "Defender a Galaxia"),
        Empresa("Avanger", "New York", "Proteger o planeta Terra"),
        Empresa("Internacional", "Avenida Padre Cacique, 891", "Vencer todos os jogos possiveis")
    ]
    lista_Remedio = [
        Remedio("Histamin","Sem Tarja","EMS"),
        Remedio("Loratadina","Sem Tarja","EMS"),
        Remedio("Buscopan","Sem Tarja","EMS")
    ]            
    lista_Funcionario = [
        Funcionario("Darth","Vader","42"),
        Funcionario("Minch","Yoda","1000"),
        Funcionario("Luke","Skywalker","62") 
    ]
    lista_livro = [
        Livro("Turma da monica","Mauricio de Souza","Panini Comics"),
        Livro("Codigo Limpo","Robert C. Martin","Alta Books"),
        Livro("O Poder do Habito","Charles Duhhigg","Objetiva")
    ]

    for empresas in lista_Empresas:
        empresas.exibir_empresa()

    for remedio in lista_Remedio:
        remedio.exibir_remedio()
        
    for funcionario in lista_Funcionario:
        funcionario.exibir_funcionario()
        
    for funcionario in lista_livro:
        funcionario.exibir_livro()
