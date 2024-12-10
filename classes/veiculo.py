# Classe Veiculo :)
class Veiculo:
    def __init__(self, marca, modelo, cor, placa, motor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.motor = motor
        
    def exibe_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Placa: {self.placa}")
        print(f"Motor: {self.motor}")