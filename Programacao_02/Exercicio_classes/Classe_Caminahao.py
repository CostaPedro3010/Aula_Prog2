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
        print(f'Testando OVERRIDE')



class Caminhao():
    def __init__(self, placa, proprietario, carga):
        self.placa = placa
        self.proprietario = proprietario
        self.nro_eixos = 3
        self.carga = carga
        self.posX = 0
        self.posY = 0
    
    def emplacamento(self, novaPlaca, novoProprietario):
        self.placa = novaPlaca
        self.proprietario = novoProprietario

    def movimento(self, incX, incY):
        self.posX += incX
        self.posY += incY

    def carga(self, incCarga):
        if(self.carga <= 100):
            self.carga += incCarga  
        elif(self.carga > 100):
            print("Carga não suportada")

    def descarga(self, decCarga):
        if(self.carga <= 99):
            self.carga -= decCarga  
        elif(self.carga < 0):
            print("Não ha o que descarregar")





class Carro(Veiculo):
    def __init__(self, placa, proprietario, ocupantes):
        super().__init__(placa, proprietario)
        self.nro_ocupantes = ocupantes

    def info(self):
        print(f"Placa: {self.placa}")
        print(f'Proprietario: {self.proprietario}')
        print(f'Nr de Ocupantes: {self.nro_ocupantes}')
        print(f'X/Y: {self.posX} / {self.posY}')

class Caminhao(Veiculo):
    def __init__(self, placa, proprietario, nro_eixos):
        super().__init__(placa, proprietario)
        self.nro_eixos = nro_eixos

    def info(self):
        print(f"Placa: {self.placa}")
        print(f'Proprietario: {self.proprietario}')
        print(f'Nro de Eixos: {self.nro_eixos}')





if __name__ == '__main__':
    c1 = Carro("JAR1E79", "ROBERTO","4")
    c1.info()
    c1.movimento(30,-19)
    c1.emplacamento("IUQ4O75","Roberto Jr")
    c1.info()

    c2 = Caminhao("JAE1E79", "ROBERTO CARDOZO", 5)
    c2.info()
