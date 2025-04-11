from enum import Enum
class Animal:
    def __init__(self, nome, especie, velocidade, habitat):
        self.nome = nome
        self.especie = especie
        self.velocidade = velocidade
        self.habitat = habitat

    def info(self):
        print("Info sobre animal cadastrado")
        print(f'{self.nome}')
        print(f'{self.especie}')
        print(f'{self.velocidade}')
        print(f'{self.habitat}')        

    
class Repteis(Animal):
    def __init__(self, nome, especie, velocidade, habitat, escama):
        super().__init__(nome, especie, velocidade, habitat)
        if( Escama.__contains__(escama)):
            self.escamas = Escama[escama].name
        else:
            #RETORNA ERRO PARA O USUARIO - OPCAO INVALIDA
            raise AttributeError("opcao invalida")
            

    def info(self):
        super().info()
        print(f'{self.escamas}')
        
class Escama(Enum):
    PLACOIDES = "PLACOIDES"
    TUBERCULADAS = "TUBERCULADAS"
    LISAS = "LISAS"
    QUILHADAS = "QUILHADAS"
    DERMICAS = "DERMICAS"  

class Aves(Animal):
    def __init__(self, nome, especie, velocidade, habitat, nro_patas):
        super().__init__(nome, especie, velocidade, habitat) 
        self.nro_patas = 2
        
if __name__ == '__main__':
    try:
        caso1 = Repteis("Lagarto", "Reptil", "15", "anfibio", "ASFJKHASFJKASHFASHFKSA")
        caso1.info()
    except AttributeError as e:
        print(e)       