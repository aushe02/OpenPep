from dataclasses import dataclass
from uilib.tools import Chemical
from uilib.fileIO import getConfigPath
from typing import List
from dependency_injector import containers, providers

import logging

@dataclass
class ChemicalManager(object):
    """This class"""

    def __init__(self):
        self.chemicalList: List[Chemical] = []
        self.load_file()

    #@inject
    def load_file(self) -> None:
        """This class loads and parses the pepcoded.daf file"""
        try:

            file = getConfigPath() + "pepcoded.daf"

            f = open(file, 'r')

            for line in f:
                flags = line[0:2].strip()
                if flags == "*" or flags == "+":
                    pass
                else:

                    lineNumber = int(line[2:8].strip())

                    name = line[9:39].strip()

                    numberOfAtomsFirstElement = int(line[39:42].strip())
                    firstElement = line[42:43].strip()

                    numberOfAtomsSecondElementElement = int(line[44:47].strip())
                    secondElement = line[47:50].strip()

                    numberOfAtomsThirdElementElementElement = int(line[50:52].strip())
                    thirdElementElement = line[52:54].strip()

                    numberOfAtomsFourthElementElementElement = int(line[54:57].strip())
                    fourthElementElement = line[57:59].strip()

                    numberOfAtomsFifthElementElementElement = int(line[59:62].strip())
                    fifthElement = line[62:64].strip()

                    numberOfAtomsSixthElementElementElement = int(line[64:67].strip())
                    sixthElement = line[67:69].strip()

                    heatOfFormation = float(line[69:74].strip())
                    density = float(line[75:80].strip())

                    # chem = providers.Factory(Chemical.Chemcial(
                    #                         flags,
                    #                          lineNumber,
                    #                          name,
                    #                          numberOfAtomsFirstElement, firstElement,
                    #                          numberOfAtomsSecondElementElement, secondElement,
                    #                          numberOfAtomsThirdElementElementElement, thirdElementElement,
                    #                          numberOfAtomsFourthElementElementElement, fourthElementElement,
                    #                          numberOfAtomsFifthElementElementElement, fifthElement,
                    #                          numberOfAtomsSixthElementElementElement, sixthElement,
                    #                          heatOfFormation,
                    #                          density))

                    chem = Chemical.Chemcial(flags,
                                             lineNumber,
                                             name,
                                             numberOfAtomsFirstElement, firstElement,
                                             numberOfAtomsSecondElementElement, secondElement,
                                             numberOfAtomsThirdElementElementElement, thirdElementElement,
                                             numberOfAtomsFourthElementElementElement, fourthElementElement,
                                             numberOfAtomsFifthElementElementElement, fifthElement,
                                             numberOfAtomsSixthElementElementElement, sixthElement,
                                             heatOfFormation,
                                             density)

                    self.chemicalList.append(chem)

            f.close()
            logging.info("Pepcoded file loaded")
        except OSError:
            logging.error(f"Could not open file: {file}")


    def getChemicalNames(self) -> List[str]:
        """This function returns a list of chemical names"""
        chemicalNameList: [str] = []
        for chemical in self.chemicalList:
            chemicalNameList.append(chemical.name)
        return chemicalNameList




