class livraria: 
    def __init__(self, editora, titulo, ano, valor, area, estoque, codigo):
        self.livros = []
        self.codigo = codigo  # Código inicial
        self.estoque = 0     # Estoque inicial
        self.editora = editora      # Editora inicial
        self.titulo = titulo       # Titulo inicial
        self.ano = ano          # Ano inicial
        self.valor = valor      # Valor inicial
        self.area = area       # Área inicial
        self.estoque = estoque     # Estoque inicial

    def cadastrar_livro(self, editora, titulo, ano, valor, area, estoque):
        # Adiciona um novo livro à lista de livros
        livro = {
            'codigo': self.codigo,
            'editora': editora,
            'titulo': titulo,
            'ano': ano,
            'valor': valor,
            'area': area,
            'estoque': estoque
        }
        self.livros.append(livro)
        self.codigo += 1
        self.estoque += estoque

    def listar_livros(self):
        # Lista todos os livros cadastrados
        for livro in self.livros:
            print(f">>>>> Cod#{livro['codigo']}")
            print(f"Titulo/Editora: {livro['titulo']}/{livro['editora']}")
            print(f"Categoria: {livro['area']}")
            print(f"Ano: {livro['ano']}")
            print(f"Valor: R$ {livro['valor']:.2f}")
            print(f"Estoque: {livro['estoque']} unidades")
            valor_total = livro['estoque'] * livro['valor']
            print(f"Valor total em estoque: R$ {valor_total:.2f}")
            print(">>>>>>")
    
    def buscar_livro_por_nome(self, nome):
        # Busca um livro pelo nome
        for livro in self.livros:
            if livro['titulo'].lower() == nome.lower():
                return livro
        return None
    
    def buscar_livros_por_preco(self, preco):
        # Busca livros com preço menor que o indicado
        livros_encontrados = []
        for livro in self.livros:
            if livro['valor'] < preco:
                livros_encontrados.append(livro)
        return livros_encontrados
    
    def buscar_livros_por_categoria(self, categoria):
        # Busca livros de uma categoria específica
        livros_encontrados = []
        for livro in self.livros:
            if livro['area'].lower() == categoria.lower():
                livros_encontrados.append(livro)
        return livros_encontrados
    
    def buscar_livros_por_estoque(self, quantidade):
        # Busca livros com valor de estoque maior que o indicado
        livros_encontrados = []
        for livro in self.livros:
            if livro['estoque'] > quantidade:
                livros_encontrados.append(livro)
        return livros_encontrados
    
    def valor_total_estoque(self):
        # Calcula o valor total em estoque de todos os livros
        valor_total = 0
        for livro in self.livros:
            valor_total += livro['estoque'] * livro['valor']
        return valor_total
    
if __name__ == '__main__':
    # Exibe o menu de opções
    print("Bem-vindo à Livraria!")
    print("Escolha uma opção:")

    # Cria uma instância da classe livraria
    livraria_instance = livraria(editora="", titulo="", ano=0, valor=0.0, area="", estoque=0, codigo=1)
    

    while True:
        print("1 – Cadastrar novo livro")
        print("2 – Listar livros")
        print("3 – Buscar livros por nome")
        print("4 – Buscar livros por categoria")
        print("5 – Buscar livros por preço")
        print("6 – Busca por quantidade em estoque")
        print("7 – Valor total no estoque")
        print("0 – Encerrar atividades")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            editora = input("Digite a editora: ")
            titulo = input("Digite o título: ")
            ano = int(input("Digite o ano: "))
            valor = float(input("Digite o valor: "))
            area = input("Digite a área: ")
            estoque = int(input("Digite a quantidade em estoque: "))
            livraria_instance.cadastrar_livro(editora, titulo, ano, valor, area, estoque)
            print("Livro cadastrado com sucesso!")
            StopIteration
        
        elif opcao == 2:
            livraria_instance.listar_livros()
        
        elif opcao == 3:
            nome = input("Digite o nome do livro: ")
            livro = livraria_instance.buscar_livro_por_nome(nome)
            if livro:
                print(f"Livro encontrado: {livro}")
            else:
                print("Livro não encontrado.")
        
        elif opcao == 4:
            categoria = input("Digite a categoria: ")
            livros_encontrados = livraria_instance.buscar_livros_por_categoria(categoria)
            if livros_encontrados:
                for livro in livros_encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado nessa categoria.")
        
        elif opcao == 5:
            preco = float(input("Digite o preço: "))
            livros_encontrados = livraria_instance.buscar_livros_por_preco(preco)
            if livros_encontrados:
                for livro in livros_encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado com preço menor que esse.")
        
        elif opcao == 6:
            quantidade = int(input("Digite a quantidade em estoque: "))
            livros_encontrados = livraria_instance.buscar_livros_por_estoque(quantidade)
            if livros_encontrados:
                for livro in livros_encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado com quantidade em estoque maior que essa.")

        elif opcao == 7:
            valor_total = livraria_instance.valor_total_estoque()
            print(f"Valor total em estoque: R$ {valor_total:.2f}")

        elif opcao == 0:
            print("Encerrando atividades...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
        print("")