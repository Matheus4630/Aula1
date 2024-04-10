
class Televisao():
    def __init__(self):
        self.power = False
        self.volume = 0
        self.canal = 1
        self.mute = False

    def ligar(self):
        if not self.power:
            self.power = True
            return True
        return False

    def desligar(self):
        if self.power:
            self.power = False
            return True
        return False

    def mutar(self):
        if not self.mute:
            self.mute = True
            return True
        return False

    def desMutar(self):
        if self.mute:
            self.mute = False
            return True
        return False

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume = self.volume + 1
        self.mute = False

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume = self.volume - 1
        self.mute = False

    def canalMais(self):
        if self.canal < 999:
            self.canal = self.canal + 1

    def canalMenos(self):
        if self.canal > 1:
            self.canal = self.canal - 1

    def numeroCanal(self, canal):
        if 0 < canal <= 999:
            self.canal = canal

    def som(self):
        if self.mute == False and self.volume > 0:
            return "som saindo da televisão"
        return "televisão sem som"

    def informacao(self):
        return f"Canal: {self.canal}, Volume: {self.volume}, mute: {self.som()}, (programação atual do self.canal)"


class Controle():
    def __init__(self, televisao):
        self.televisao = televisao

    def botaoPower(self):
        if self.televisao.ligar():
            return
        elif self.televisao.desligar():
            return
        "solucionar o problema da televisão ou controle"

    def botaoMute(self):
        if self.televisao.mutar():
            return
        self.televisao.desMutar()
        return

    def volumeMais(self):
        self.televisao.aumentarVolume()

    def volumeMenos(self):
        self.televisao.diminuirVolume()

    def getInfo(self):
        return self.televisao.informacao()

    def canalCima(self):
        self.televisao.canalMais()

    def canalBaixo(self):
        self.televisao.canalMenos()

    def digitarCanal(self, numero, canal=None):
        canal = f"{canal}{numero}"
        while "digitarem outro numero em menos de 5 segundos após o anterior":
            canal = f"{canal}{numero}"
        self.televisao.numeroCanal(canal)

    def numero1(self):
        self.digitarCanal(1)

    def numero2(self):
        self.digitarCanal(2)

    def numero3(self):
        self.digitarCanal(3)

    def numero4(self):
        self.digitarCanal(4)

    def numero5(self):
        self.digitarCanal(5)

    def numero6(self):
        self.digitarCanal(6)

    def numero7(self):
        self.digitarCanal(7)

    def numero8(self):
        self.digitarCanal(8)

    def numero9(self):
        self.digitarCanal(9)

    def numero0(self):
        self.digitarCanal(0)


TV = Televisao()
controle = Controle(TV)
