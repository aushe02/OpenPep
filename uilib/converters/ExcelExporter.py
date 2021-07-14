from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Propellant designation"
sheet["B1"] = "world!"

sheet["A2"] = "Propellant density"
sheet["B2"] = "world!"
sheet["C2"] = "lb/in^3"


sheet["A5"] = "Diameter (in)"
sheet["A6"] = "Length (in)"
sheet["A7"] = "Core (in)"
sheet["A8"] = "Number of grains"
sheet["A9"] = "Expected waste"



workbook.save(filename="hello_world.xlsx")