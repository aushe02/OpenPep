from dataclasses import dataclass


# from dependency_injector import containers, providers

@dataclass
class Chemcial(object):
    """Class that represents a pepcoded chemical entry"""

    def __init__(self,
                 flags: str,
                 lineNumber: int,
                 name: str,
                 numberOfAtomsFirstElement: int,
                 firstElement: str,
                 numberOfAtomsSecondElement: int,
                 secondElement: str,
                 numberOfAtomsThirdElement: int,
                 thirdElement: str,
                 numberOfAtomsFourthElement: int,
                 fourthElement: str,
                 numberOfAtomsFifthElement: int,
                 fifthElement: str,
                 numberOfAtomsSixthElement: int,
                 sixthElement: str,
                 heatOfFormation: float,
                 density: float
                 ) -> None:
        self.flags = flags
        self.lineNumber = lineNumber
        self.name = name
        self.numberOfAtomsFirstElement = numberOfAtomsFirstElement
        self.firstElement = firstElement
        self.numberOfAtomsSecondElement = numberOfAtomsSecondElement
        self.secondElement = secondElement
        self.numberOfAtomsThirdElement = numberOfAtomsThirdElement
        self.thirdElement = thirdElement
        self.numberOfAtomsFourthElement = numberOfAtomsFourthElement
        self.fourthElement = fourthElement
        self.numberOfAtomsFifthElement = numberOfAtomsFifthElement
        self.fifthElement = fifthElement
        self.numberOfAtomsSixthElement = numberOfAtomsSixthElement
        self.sixthElement = sixthElement
        self.heatOfFormation = heatOfFormation
        self.density = density
