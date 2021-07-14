from dataclasses import dataclass


@dataclass(frozen=False)
class FormulaResult():

    def __init__(self,
                 ispResult: float,
                 cStarResult: float,
                 densityResult: float,
                 chamberTempResult: float,
                 chamberCPCVResult: float,
                 molecularWtResult: float):
        self.ispResult = ispResult
        self.cStarResult = cStarResult
        self.densityResult = densityResult
        self.chamberTempResult = chamberTempResult
        self.chamberCPCVResult = chamberCPCVResult
        self.molecularWtResult = molecularWtResult
