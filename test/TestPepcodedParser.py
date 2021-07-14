import unittest
import uilib.tools.Pepcodedparser


class TestPepcodedParser(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # def test_failed_file_open(self):
    #     self.assertEqual("Could not open file: resources/pepcoded",
    #                      uilib.tools.Pepcodedparser.load_file("resources/pepcoded"), "Failed to open file")

    def test_acetamide(self):

        test_line = 1

        uilib.tools.Pepcodedparser.load_file(
            "/Users/austinheisey/Documents/GitHub/OpenPep/resources/pepcoded.daf")
        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].flags, "Test acetamide flags")
        self.assertEqual(30, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].lineNumber,
                         "Test acetamide line number")
        self.assertEqual("ACETAMIDE", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].name, "Test acetamide name")
        self.assertEqual(2, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFirstElement,
                         "Test acetamide number of atoms first element")
        self.assertEqual("C", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].firstElement,
                         "Test acetamide first element")
        self.assertEqual(5, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsSecondElement,
                         "Test acetamide number of atoms second element")
        self.assertEqual("H", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].secondElement,
                         "Test acetamide second element")
        self.assertEqual(1, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsThirdElement,
                         "Test acetamide number of atoms third element")
        self.assertEqual("O", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].thirdElement,
                         "Test acetamide third element")
        self.assertEqual(1, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFourthElement,
                         "Test acetamide number of atoms fourth element")
        self.assertEqual("N", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].fourthElement,
                         "Test acetamide fourth element")
        self.assertEqual(0, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFifthElement,
                         "Test acetamide number of atoms fifth element")
        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].fifthElement,
                         "Test acetamide fifth element")
        self.assertEqual(0, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsSixthElement,
                         "Test acetamide number of atoms sixth element")

        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].sixthElement,
                         "Test acetamide sixth element")
        self.assertEqual(-1310, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].heatOfFormation,
                         "Test acetamide heat formation")
        self.assertEqual(.0360, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].density, "Test acetamide density")

    def test_acrylonitrile(self):

        test_line = 9

        uilib.tools.Pepcodedparser.load_file(
            "/Users/austinheisey/Documents/GitHub/OpenPep/resources/pepcoded.daf")
        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].flags, "Test acrylonitrile flags")
        self.assertEqual(38, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].lineNumber,
                         "Test acrylonitrile line number")
        self.assertEqual("ACRYLONITRILE", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].name,
                         "Test acrylonitrile name")
        self.assertEqual(575, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFirstElement,
                         "Test acrylonitrile number of atoms first element")
        self.assertEqual("C", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].firstElement,
                         "Test acrylonitrile first element")
        self.assertEqual(609, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsSecondElement,
                         "Test acrylonitrile number of atoms second element")
        self.assertEqual("H", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].secondElement,
                         "Test acrylonitrile second element")
        self.assertEqual(8, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsThirdElement,
                         "Test acrylonitrile number of atoms third element")
        self.assertEqual("O", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].thirdElement,
                         "Test acrylonitrile third element")
        self.assertEqual(169, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFourthElement,
                         "Test acrylonitrile number of atoms third element")
        self.assertEqual("N", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].fourthElement,
                         "Test acrylonitrile fourth element")
        self.assertEqual(0, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFifthElement,
                         "Test acrylonitrile number of atoms fifth element")
        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].fifthElement,
                         "Test acrylonitrile fifth element")

        self.assertEqual(0, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsSixthElement,
                         "Test acrylonitrile number of atoms sixth element")

        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].sixthElement,
                         "Test acrylonitrile sixth element")

        self.assertEqual(334, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].heatOfFormation,
                         "Test acrylonitrile heat formation")
        self.assertEqual(.0000, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].density,
                         "Test acrylonitrile density")



    def test_e107_a_mixture(self):
        test_line = 337

        uilib.tools.Pepcodedparser.load_file(
            "/Users/austinheisey/Documents/GitHub/OpenPep/resources/pepcoded.daf")
        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].flags, "Test E107  (A MIXTURE) flags")
        self.assertEqual(379, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].lineNumber,
                         "Test E107  (A MIXTURE) line number")
        self.assertEqual("E107  (A MIXTURE)", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].name,
                         "Test E107  (A MIXTURE) name")
        self.assertEqual(441, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFirstElement,
                         "Test E107  (A MIXTURE) number of atoms first element")
        self.assertEqual("H", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].firstElement,
                         "Test E107  (A MIXTURE) first element")
        self.assertEqual(133, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsSecondElement,
                         "Test E107  (A MIXTURE) number of atoms second element")
        self.assertEqual("C", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].secondElement,
                         "Test E107  (A MIXTURE) second element")
        self.assertEqual(52, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsThirdElement,
                         "Test E107  (A MIXTURE) number of atoms third element")
        self.assertEqual("N", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].thirdElement,
                         "Test E107  (A MIXTURE) third element")
        self.assertEqual(232, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFourthElement,
                         "Test E107  (A MIXTURE) number of atoms third element")
        self.assertEqual("O", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].fourthElement,
                         "Test E107  (A MIXTURE) fourth element")
        self.assertEqual(6, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFifthElement,
                         "Test E107  (A MIXTURE) number of atoms fifth element")
        self.assertEqual("AL", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].fifthElement,
                         "Test E107  (A MIXTURE) fifth element")

        self.assertEqual(49, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsSixthElement,
                         "Test E107  (A MIXTURE) number of atoms sixth element")

        self.assertEqual("CL", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].sixthElement,
                         "Test E107  (A MIXTURE) sixth element")

        self.assertEqual(-552, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].heatOfFormation,
                         "Test E107  (A MIXTURE) heat formation")
        self.assertEqual(.0604, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].density,
                         "Test E107  (A MIXTURE) density")

    #ACETYLENE (LIQUID)
    def test_acetylene_liquid(self):
        test_line = 3

        uilib.tools.Pepcodedparser.load_file(
            "/Users/austinheisey/Documents/GitHub/OpenPep/resources/pepcoded.daf")
        self.assertEqual("BD", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].flags, "Test E107  (A MIXTURE) flags")
        self.assertEqual(32, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].lineNumber,
                         "Test E107  (A MIXTURE) line number")
        self.assertEqual("ACETYLENE (LIQUID)", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].name,
                         "Test E107  (A MIXTURE) name")
        self.assertEqual(2, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFirstElement,
                         "Test E107  (A MIXTURE) number of atoms first element")
        self.assertEqual("C", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].firstElement,
                         "Test E107  (A MIXTURE) first element")
        self.assertEqual(2, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsSecondElement,
                         "Test E107  (A MIXTURE) number of atoms second element")
        self.assertEqual("H", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].secondElement,
                         "Test E107  (A MIXTURE) second element")
        self.assertEqual(0, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsThirdElement,
                         "Test E107  (A MIXTURE) number of atoms third element")
        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].thirdElement,
                         "Test E107  (A MIXTURE) third element")
        self.assertEqual(0, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFourthElement,
                         "Test E107  (A MIXTURE) number of atoms third element")
        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].fourthElement,
                         "Test E107  (A MIXTURE) fourth element")
        self.assertEqual(0, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsFifthElement,
                         "Test E107  (A MIXTURE) number of atoms fifth element")
        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].fifthElement,
                         "Test E107  (A MIXTURE) fifth element")

        self.assertEqual(0, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].numberOfAtomsSixthElement,
                         "Test E107  (A MIXTURE) number of atoms sixth element")

        self.assertEqual("", uilib.tools.Pepcodedparser.cm.chemicalList[test_line].sixthElement,
                         "Test E107  (A MIXTURE) sixth element")

        self.assertEqual(1846, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].heatOfFormation,
                         "Test E107  (A MIXTURE) heat formation")
        self.assertEqual(0.0263, uilib.tools.Pepcodedparser.cm.chemicalList[test_line].density,
                         "Test E107  (A MIXTURE) density")