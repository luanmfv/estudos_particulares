#Class
#Syntaxe

#Marca, Memoria Ram, Placa de vídeo
#__init__ da a funcionalidade para o class
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass

computador1 = Computador('Asus','8gb','Nvidia')
computador2 = Computador('Dell','10gb','GeForce')
computador3 = Computador('Acer','16gb','ATM')  
print(computador1.marca,computador1.memoria_ram,computador1.placa_de_video)
print(computador2.marca,computador2.memoria_ram,computador2.placa_de_video)
print(computador3.marca,computador3.memoria_ram,computador3.placa_de_video)

print('-' *30)

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou desligando')
    
    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Asus','16Gb','Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()

#Ligar, Desligar, Exibir Configurações



























































