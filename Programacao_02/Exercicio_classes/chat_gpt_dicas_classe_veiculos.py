class Carro:
    def __init__(self):
        self.placa = None
        self.proprietario = None
        self.posicaoX = 0
        self.posicaoY = 0

    def cadastrar_carro(self, placa, proprietario, posicaoX, posicaoY):
        self.placa = placa
        self.proprietario = proprietario
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY

    def emplacar(self, nova_placa, novo_proprietario):
        self.placa = nova_placa
        self.proprietario = novo_proprietario

    def movimentar(self, deslocamentoX, deslocamentoY):
        self.posicaoX += deslocamentoX
        self.posicaoY += deslocamentoY
        print(f"Carro movimentado para nova posição: X={self.posicaoX}, Y={self.posicaoY}")

    def mostrar_informacoes(self):
        print(f"Placa: {self.placa}")
        print(f"Proprietário: {self.proprietario}")
        print(f"Posição X: {self.posicaoX}")
        print(f"Posição Y: {self.posicaoY}")
