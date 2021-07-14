from uilib.tools.Chemical import Chemcial
from uilib.ChemicalManager import ChemicalManager
from uilib.fileIO import getConfigPath

from typing import TextIO

chemicalManager = ChemicalManager()


def load_file(file: str):
    try:
        f = open(file, 'r')
        parse_file(f)
        f.close()
    except OSError:
        print(f"Could not open file: {file}")


def parse_file(lines: TextIO):
    for line in lines:
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

            chem = Chemcial(flags,
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

            chemicalManager.chemicalList.append(chem)


#     print(chemicalManager.chemicalList[0].numberOfAtomsFirstElement)
#
#     print(len(chemicalManager.chemicalList))
#
#
# if __name__ == "__main__":
#     pepcodedFile = getConfigPath() + "pepcoded.daf"
#     cm = load_file(pepcodedFile)
