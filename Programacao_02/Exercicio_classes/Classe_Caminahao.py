class Veiculo:
    def __init__(self, placa, proprietario):
        self.placa = placa
        self.proprietario = proprietario
        self.posX = 0
        self.posY = 0

    def emplacamento(self, novaPlaca, novoProprietario):
        self.placa = novaPlaca
        self.proprietario = novoProprietario
    
    def movimento(self, incX, incY):
        self.posX += incX
        self.posY += incY
    
    def info(self):
        print(f"Placa: {self.placa}")
        print(f"Proprietario: {self.proprietario}")
        print(f"X/Y: {self.posX} / {self.posY}")


class VeiculoCarga(Veiculo):
    def __init__(self, placa, proprietario, carga=0):
        super().__init__(placa, proprietario)
        self.carga = carga

    def adicionar_carga(self, incCarga):
        if self.carga + incCarga <= 100:
            self.carga += incCarga  
        else:
            print("Carga não suportada")

    def remover_carga(self, decCarga):
        if self.carga - decCarga >= 0:
            self.carga -= decCarga  
        else:
            print("Não há o que descarregar")


class Caminhao(VeiculoCarga):
    def __init__(self, placa, proprietario, nro_eixos):
        super().__init__(placa, proprietario, carga=0)
        self.nro_eixos = nro_eixos

    def info(self):
        super().info()
        print(f"Número de eixos: {self.nro_eixos}")
        print(f"Carga: {self.carga}")


class Carro(Veiculo):
    def __init__(self, placa, proprietario, ocupantes):
        super().__init__(placa, proprietario)
        self.nro_ocupantes = ocupantes


if __name__ == '__main__':
    c1 = Carro("JAR1E79", "ROBERTO", "4")
    c1.info()
    c1.movimento(30, -19)
    c1.emplacamento("IUQ4O75", "Roberto Jr")
    c1.info()


    c2 = Caminhao("JAE1E79", "ROBERTO CARDOZO", 5)
    c2.info()
    c2.adicionar_carga(44)
    c2.remover_carga(40)
    c2.info()