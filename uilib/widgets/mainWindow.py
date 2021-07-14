import logging

from uilib.tools import Ingredient
from PyQt5.QtWidgets import QMainWindow, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
import uilib.widgets.aboutDialog
import uilib.widgets.pepcodedUiEditor
from uilib.views.MainWindow_ui import Ui_MainWindow
from uilib import ChemicalManager
from uilib.tools import PropellantFormula
from uilib import OperatingConditionsManager
from PyQt5 import QtWidgets



class Window(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, app):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.app = app

        self.setWindowIcon(self.app.icon)

        self.appVersion = uilib.fileIO.appVersion
        self.appVersionStr = uilib.fileIO.appVersionStr

        self.updateWindowTitle("None", False)

        self.aboutDialog = uilib.widgets.aboutDialog.AboutDialog(self.appVersionStr)
        self.pepcodedEditorDialog = uilib.widgets.pepcodedUiEditor.PepcodedUiEditor(self.appVersionStr)

        self.setupMenu()

        self.listFormulaIngredients: Ingredient =[]
        opt = OperatingConditionsManager.OperatingConditionsManager()
        #pm = PropellantFormula.PropellantFormula()
        chemicalManager = ChemicalManager.ChemicalManager()
        listChem = chemicalManager.getChemicalNames()

        self.ui.formulaTableWidgetList.setColumnCount(3)

        self.ui.comboBoxChemical.addItems(listChem)
        self.ui.doubleSpinBoxChemicalAmount.value()
        #self.ui.groupBoxFormulaResults

        self.ui.addChemicalPushButton.pressed.connect(self.addChemical)
        self.ui.removeChemicalPushButton.pressed.connect(self.deleteChemical)
        self.ui.editChemicalPushButton.pressed.connect(self.editChemical)



        self.row: int = 0
        self.col: int = 0




    def updateWindowTitle(self, name: str, saved: bool):
        if not name and saved:
            self.setWindowTitle('openPep')
            return
        unsavedStr = '*' if not saved else ''
        displayName = name if name is not None else ''
        self.setWindowTitle('openPep - {}{}'.format(displayName, unsavedStr))

    def setupMenu(self):
        # File menu

        # Edit Menu
        #self.ui.actionUndo.triggered.connect(self.undo)
        #self.ui.actionRedo.triggered.connect(self.redo)

        # Help
        self.ui.actionAboutOpenPep.triggered.connect(self.aboutDialog.show)
        self.ui.actiontest12.triggered.connect(self.aboutDialog.show)
        self.ui.actionPepcoded_File.triggered.connect(self.pepcodedEditorDialog.show)

    # def undo(self):
    #     pass
    #
    # def redo(self):
    #     pass
    #
    # def checkChemicalSelection(self):
    #     ind = self.formulaTableWidgetList.selectionModel().selectedRows()
    #     if len(ind) > 0:
    #         grid = ind[0].row
    #
    #
    def deleteChemical(self):
        ind = self.ui.formulaTableWidgetList.selectionModel().selectedRows()
        #self.chemicalManager.
        print(ind)

    def editChemical(self):
        ind = self.ui.formulaTableWidgetList.selectionModel().selectedRows()
        print(ind)

    def updateChemicalTable(self):
        pass


    def addChemical(self):
        chemical = self.ui.comboBoxChemical.currentText()
        amount = self.ui.doubleSpinBoxChemicalAmount.value()
        self.listFormulaIngredients.append(Ingredient.Ingredient(chemical, amount))
        self.ui.formulaTableWidgetList.setRowCount(len(self.listFormulaIngredients))

        self.addChemicalTable(chemical, str(amount), "g")


    def addChemicalTable(self, chemical: str, amount: str, unit: str):
        self.ui.formulaTableWidgetList.setItem(self.row, 0, QtWidgets.QTableWidgetItem(chemical))
        self.ui.formulaTableWidgetList.setItem(self.row, 1, QtWidgets.QTableWidgetItem(amount))
        self.ui.formulaTableWidgetList.setItem(self.row, 2, QtWidgets.QTableWidgetItem(unit))
        self.row+=1

    def setFormulaCalcualtionResult(self, ispResult: str, tempResult: str, CPCVResult: str, densityResult: str, cResult: str, molecularWtResult: str):
        self.ui.labelIspResult.setText(ispResult)
        self.ui.labelChamberTempResult.setText(tempResult)
        self.ui.labelChamberCPCVResult.setText(CPCVResult)
        self.ui.labelDensityResult.setText(densityResult)
        self.ui.labelCResult.setText(cResult)
        self.ui.labelMolecularWtResult.setText(molecularWtResult)

    def setOperatingCondidtions(self, tempOfIngredients: float, chamberPressure: float, exhaustPressure: float):
        self.ui.tempOfIngredientsDoubleSpinBox.setValue(tempOfIngredients)
        self.ui.chamberPressureDoubleSpinBox.setValue(chamberPressure)
        self.ui.exhaustPressureDoubleSpinBox.setValue(exhaustPressure)



    # def editChemical(self):
    #     pass
    #
    # def setupFormulaTable(self):
    #     self.ui.formulaTableWidgetList.clearContent()
    #
    #     header = self.ui.formulaTableWidgetList.horizontalHeader()
    #     header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    #     header.setSectionResizeMode(1, QHeaderView.Stretch)
    #
    #     #self.updateFormulaTable()
    #     self.ui.removeaddChemicalPushButton.pressed.connect(self.deleteGrain)
    #     #self.ui.addChemicalPushButton.pressed.connec
    #
    # def keyPressEvent(self, event) -> None:
    #     if event.key() == Qt.Key_Delete or event.key() == Qt.Key_Backspace:
    #         if len(self.ui.formulaTableWidgetList.selectedItems() != 0):
    #             self.deleteGrain()
