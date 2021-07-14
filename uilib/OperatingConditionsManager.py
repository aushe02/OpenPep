from PyQt5.QtCore import QObject, pyqtSignal

class OperatingConditionsManager(QObject):

    updated = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.temp: float = 298
        self.chamberPressure: float = 1000
        self.exhaustPressure: float = 14.70

    def setTemp(self, temp: float):
        self.temp = temp

    def getTemp(self):
        return self.temp