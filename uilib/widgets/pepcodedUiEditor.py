import logging

from PyQt5.QtWidgets import QDialog, QHeaderView
from PyQt5 import QtWidgets
from uilib.tools import Chemical

from ..views.PepcodedEditor_ui import Ui_Form
from uilib import ChemicalManager


class PepcodedUiEditor(QDialog):

    def __init__(self, version):
        QDialog.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        chemicalManager = ChemicalManager.ChemicalManager()

        self.ui.formulaTableWidgetList.setRowCount(len(chemicalManager.chemicalList))
        self.ui.formulaTableWidgetList.setColumnCount(16)

        self.ui.pushButtonEdit.pressed.connect(self.editEntry)
        self.ui.pushButtonAdd.pressed.connect(self.addEntry)
        self.ui.pushButtonDelete.pressed.connect(self.removeEntry)
        self.ui.pushButtonClose.pressed.connect(self.close)

        header = self.ui.formulaTableWidgetList.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        col = 0

        for chemical in chemicalManager.chemicalList:
            self.populateTable(chemical, col)
            col += 1

    def populateTable(self, chemical: Chemical, col: int) -> None:
        self.ui.formulaTableWidgetList.setItem(col, 0, QtWidgets.QTableWidgetItem(chemical.flags))
        self.ui.formulaTableWidgetList.setItem(col, 1, QtWidgets.QTableWidgetItem(chemical.name))
        self.ui.formulaTableWidgetList.setItem(col, 2,
                                               QtWidgets.QTableWidgetItem(str(chemical.numberOfAtomsFirstElement)))
        self.ui.formulaTableWidgetList.setItem(col, 3, QtWidgets.QTableWidgetItem(chemical.firstElement))
        self.ui.formulaTableWidgetList.setItem(col, 4,
                                               QtWidgets.QTableWidgetItem(str(chemical.numberOfAtomsSecondElement)))
        self.ui.formulaTableWidgetList.setItem(col, 5, QtWidgets.QTableWidgetItem(chemical.secondElement))
        self.ui.formulaTableWidgetList.setItem(col, 6,
                                               QtWidgets.QTableWidgetItem(str(chemical.numberOfAtomsThirdElement)))
        self.ui.formulaTableWidgetList.setItem(col, 7, QtWidgets.QTableWidgetItem(chemical.thirdElement))
        self.ui.formulaTableWidgetList.setItem(col, 8,
                                               QtWidgets.QTableWidgetItem(str(chemical.numberOfAtomsFourthElement)))
        self.ui.formulaTableWidgetList.setItem(col, 9, QtWidgets.QTableWidgetItem(chemical.fourthElement))
        self.ui.formulaTableWidgetList.setItem(col, 10,
                                               QtWidgets.QTableWidgetItem(str(chemical.numberOfAtomsFifthElement)))
        self.ui.formulaTableWidgetList.setItem(col, 11, QtWidgets.QTableWidgetItem(chemical.fifthElement))
        self.ui.formulaTableWidgetList.setItem(col, 12,
                                               QtWidgets.QTableWidgetItem(str(chemical.numberOfAtomsSixthElement)))
        self.ui.formulaTableWidgetList.setItem(col, 13, QtWidgets.QTableWidgetItem(chemical.sixthElement))
        self.ui.formulaTableWidgetList.setItem(col, 14, QtWidgets.QTableWidgetItem(str(chemical.heatOfFormation)))
        self.ui.formulaTableWidgetList.setItem(col, 15, QtWidgets.QTableWidgetItem(str(chemical.density)))

    def addEntry(self):
        print("Add Entry")

    def editEntry(self):
        ind = self.ui.formulaTableWidgetList.selectionModel().selectedRows()
        if len(ind) > 0:
            grid = ind[0].row()
            chemical = chemicalManager.chemicalList[grid]
            self.setChemicalEditorValues(chemical.name, chemical.firstElement)



    def removeEntry(self):
        print("Remove Entry")

    def setChemicalEditorValues(self, chemicalName: str, firstElementNumber: float, firstElement: str):
        self.ui.labelChemicalName.setText(chemicalName)
        self.ui.spinBoxFirstElementNumber.setValue(firstElementNumber)

