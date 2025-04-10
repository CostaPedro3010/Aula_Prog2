# Estrutura para armazenar os livros
livros = []

# Função para cadastrar um novo livro
def cadastrar_livro():
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ")
    codigo = input("Código: ")
    editora = input("Editora: ")
    area = input("Categoria: ")
    ano = int(input("Ano: "))
    valor = float(input("Valor (R$): "))
    estoque = int(input("Quantidade em estoque: "))
    
    livro = {
        'titulo': titulo,
        'codigo': codigo,
        'editora': editora,
        'area': area,
        'ano': ano,
        'valor': valor,
        'estoque': estoque
    }
    livros.append(livro)
    print("Livro cadastrado com sucesso!\n")

# Função para listar todos os livros
def listar_livros():
    print("\n--- Lista de Livros ---")
    for livro in livros:
        valor_total = livro['valor'] * livro['estoque']
        print(f">>>>> Cod#{livro['codigo']}")
        print(f"Título/Editora: {livro['titulo']}/{livro['editora']}")
        print(f"Categoria: {livro['area']}")
        print(f"Ano: {livro['ano']}")
        print(f"Valor: R$ {livro['valor']:.2f}")
        print(f"Estoque: {livro['estoque']} unidades")
        print(f"Valor total em estoque: R$ {valor_total:.2f}")
        print("-------------------------")

# Buscar livro por nome
def buscar_por_nome():
    nome = input("Digite o nome do livro: ").lower()
    encontrados = [livro for livro in livros if nome in livro['titulo'].lower()]
    if encontrados:
        for livro in encontrados:
            print(f"{livro['titulo']} - R$ {livro['valor']}")
    else:
        print("Nenhum livro encontrado com esse nome.")

# Buscar por categoria
def buscar_por_categoria():
    categoria = input("Digite a categoria: ").lower()
    encontrados = [livro for livro in livros if categoria in livro['area'].lower()]
    if encontrados:
        for livro in encontrados:
            print(f"{livro['titulo']} - Categoria: {livro['area']}")
    else:
        print("Nenhum livro encontrado nessa categoria.")

# Buscar por valor menor que o informado
def buscar_por_preco():
    preco = float(input("Listar livros com preço menor que: R$ "))
    encontrados = [livro for livro in livros if livro['valor'] < preco]
    if encontrados:
        for livro in encontrados:
            print(f"{livro['titulo']} - R$ {livro['valor']}")
    else:
        print("Nenhum livro encontrado com valor menor que isso.")

# Buscar por valor total em estoque maior que
def buscar_por_valor_estoque():
    valor = float(input("Buscar livros com valor total em estoque maior que: R$ "))
    encontrados = [livro for livro in livros if livro['valor'] * livro['estoque'] > valor]
    if encontrados:
        for livro in encontrados:
            valor_total = livro['valor'] * livro['estoque']
            print(f"{livro['titulo']} - Valor em estoque: R$ {valor_total:.2f}")
    else:
        print("Nenhum livro encontrado com esse valor em estoque.")

# Mostrar valor total de todos os livros no estoque
def valor_total_estoque():
    total = sum(livro['valor'] * livro['estoque'] for livro in livros)
    print(f"\nValor total de todos os livros no estoque: R$ {total:.2f}")

# Menu principal
def menu():
    while True:
        print("\n====== Menu ======")
        print("1 – Cadastrar novo livro")
        print("2 – Listar livros")
        print("3 – Buscar livros por nome")
        print("4 – Buscar livros por categoria")
        print("5 – Buscar livros por preço")
        print("6 – Busca por valor total em estoque")
        print("7 – Valor total no estoque")
        print("0 – Encerrar atividades")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_por_nome()
        elif opcao == '4':
            buscar_por_categoria()
        elif opcao == '5':
            buscar_por_preco()
        elif opcao == '6':
            buscar_por_valor_estoque()
        elif opcao == '7':
            valor_total_estoque()
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu()
