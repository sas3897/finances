import sys


class TaxBracket:
    def __init__(self, perc, cap):
        self.perc = perc
        self.cap = cap

# SINGLE BRACKETS
federal_brackets_single = [
    TaxBracket(0, 0),
    TaxBracket(.1, 9700),
    TaxBracket(.12, 39475),
    TaxBracket(.22, 84200),
    TaxBracket(.24, 160725),
    TaxBracket(.32, 204100),
    TaxBracket(.35, 510300),
    TaxBracket(.37, sys.maxsize)
]
md_brackets_single = [
    TaxBracket(0, 0),
    TaxBracket(.02, 1000),
    TaxBracket(.03, 2000),
    TaxBracket(.04, 3000),
    TaxBracket(.0475, 100000),
    TaxBracket(.05, 125000),
    TaxBracket(.0525, 150000),
    TaxBracket(.055, 250000),
    TaxBracket(.0575, sys.maxsize)
]
ny_brackets_single = [
    TaxBracket(0, 0),
    TaxBracket(.04, 8500),
    TaxBracket(.045, 11700),
    TaxBracket(.0525, 13900),
    TaxBracket(.059, 21400),
    TaxBracket(.0633, 80650),
    TaxBracket(.0657, 215400),
    TaxBracket(.0685, 1077550),
    TaxBracket(.0882, sys.maxsize)
]

# MARRIED BRACKETS
federal_brackets_married = [
    TaxBracket(0, 0),
    TaxBracket(.1, 19400),
    TaxBracket(.12, 78950),
    TaxBracket(.22, 168400),
    TaxBracket(.24, 321450),
    TaxBracket(.32, 408200),
    TaxBracket(.35, 612350),
    TaxBracket(.37, sys.maxsize)
]
md_brackets_married = [
    TaxBracket(0, 0),
    TaxBracket(.02, 1000),
    TaxBracket(.03, 2000),
    TaxBracket(.04, 3000),
    TaxBracket(.0475, 150000),
    TaxBracket(.05, 175000),
    TaxBracket(.0525, 225000),
    TaxBracket(.055, 300000),
    TaxBracket(.0575, sys.maxsize)
]
ny_brackets_married = [
    TaxBracket(0, 0),
    TaxBracket(.04, 17150),
    TaxBracket(.045, 23600),
    TaxBracket(.0525, 27900),
    TaxBracket(.059, 43000),
    TaxBracket(.0633, 161550),
    TaxBracket(.0657, 323200),
    TaxBracket(.0685, 2155350),
    TaxBracket(.0882, sys.maxsize)
]

# FLAT "BRACKETS"
moco_bracket = [
    TaxBracket(0, 0),
    TaxBracket(.032, sys.maxsize)
]
