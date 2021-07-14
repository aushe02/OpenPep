from uilib.tools.Chemical import Chemcial
from dataclasses import dataclass

@dataclass
class Ingredient(object):

    def __init__(self, chemical: str, weight: float):
        self.chemical = chemical
        self.weight = weight