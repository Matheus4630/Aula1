
class Televisao():
    def __init__(self):
        self.power = False
        self.volume = 0
        self.canal = 1
        self.mute = False

    def ligar(self):
        self.power = True

    def desligar(self):
        self.power = False

    def mutar(self):
        self.mute = True

    def desMutar(self):
        self.mute = False

    def volumeMais(self):
        if self.volume < 100:
            self.volume = self.volume + 1

    def volumeMenos(self):
        if self.volume > 0:
            self.volume = self.volume - 1

    def canalMais(self):
        self.canal = self.canal + 1

    def canalMenos(self):
        if self.canal > 1:
            self.canal = self.canal - 1

    def digitarCanal(self, canal):
        self.canal = canal

    def som(self):
        if self.mute == False and self.volume > 0:
            return "som saindo da televisão"

    def getInfo(self):
        return self.canal."informações da programação atual"
