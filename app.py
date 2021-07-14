import logging

import uilib.widgets.mainWindow
from uilib.fileIO import getConfigPath
from PyQt5.QtGui import QIcon
from uilib import ChemicalManager, OperatingConditionsManager

from PyQt5.QtWidgets import QApplication


class App(QApplication):

    NAME = 'OpenPep'
    VERSION = (0, 0, 1)

    def __init__(self, args):
        super().__init__(args)

        self.icon = QIcon('resources/icons/template_icon.png')

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(getConfigPath() + "openPep.log"),
                logging.StreamHandler()
            ]
        )

        logging.info("OpenPep Started")

        self.chemicalManager = ChemicalManager.ChemicalManager()
        self.operatingConditionManager = OperatingConditionsManager.OperatingConditionsManager()

        print(self.chemicalManager.chemicalList[1].name)
        print(self.operatingConditionManager.getTemp())

        logging.info('Opening main window')
        self.window = uilib.widgets.mainWindow.Window(self)

        self.window.show()
        logging.info('Main window open')

