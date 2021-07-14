import uilib.OperatingConditionsManager

class PropellantFormula:

    def __init__(self, listIngredients: list, operatingConditions: uilib.OperatingConditionsManager):
        self.listIngredients = listIngredients
        self.operatingConditions = operatingConditions