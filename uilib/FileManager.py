from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import logging
from uilib.tools import PropellantFormula

class FileManager(QObject):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.fileHistory = []
        self.currentVersion = 0
        self.savedVersion = 0
        self.fileName = None
        self.newFile()

    def newFile(self):
        if not self.unsavedCheck():
            logging.log("Cannot start new file because of existing one")
            return
        logging.log("Starting new propellant file")
        newPropellant = PropellantFormula.PropellantFormula()



    def save(self):
        if self.fileName is None:
            self.saveAs()

    def saveAs(self):
        fileName = self.showSaveDialog()
        if fileName is not None:
            self.fileName = fileName
            self.save()

    def load(self):
        pass

