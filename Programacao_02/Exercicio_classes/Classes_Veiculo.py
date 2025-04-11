class carro:
    def cadastro_carro(self, placa, proprietario, posicaoX, posicaoY):
        self.placa = placa
        self.proprietario = proprietario
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY
    
    
    def emplacamento(self, nova_placa, novo_proprietario):
        self.placa = nova_placa
        self.proprietario = novo_proprietario

    def movimento(self, deslocamentoX, deslocamentoY):
        self.posicaoX += deslocamentoX
        self.posicaoY += deslocamentoY
        print(f"seu carro se moveu para a posição: X={self.posicaoX}, Y={self.posicaoY}")

    def mostrar_informacoes_carros(self):
        print(f"Placa: {self.placa}")
        print(f"Proprietario: {self.proprietario}")
        print(f"Posicao X: {self.posicaoX}")
        print(f"Posicao Y: {self.posicaoY}")


carro = carro()
carro.cadastro_carro("ABC1234", "João", 10, 20)
carro.mostrar_informacoes_carros()

print("\n--- Movimento ---")
carro.movimento(5, -55)  

print("\n--- Informações Atualizadas ---")
carro.mostrar_informacoes_carros()

print("\n--- Emplacamento ---")
carro.emplacamento("XYZ9876", "Maria")
carro.mostrar_informacoes_carros()





























