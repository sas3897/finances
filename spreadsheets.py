import sys

class TaxBracket:
    def __init__(self, perc, cap):
        self.perc = perc
        self.cap = cap

    def over_cap():
        return self.perc * self.cap


def four_oh_one_k():
    pass


# This function assumes that your income is below the cap of at least one
# tax bracket in tax_brackets, as this is how all tax_brackets I know of work
def taxes_calc(adjusted_income, tax_brackets):
    after_tax = adjusted_income
    last_bracket = True

    for tax_idx in range(0, len(tax_brackets)):
        curr_tax = tax_brackets[tax_idx]
        last_bracket = adjusted_income < curr_tax.cap

        if last_bracket:
            if tax_idx == 0:
                return adjusted_income * (1-curr_tax.perc)
            return after_tax - ((adjusted_income - (tax_brackets[tax_idx-1].cap + 1)) * curr_tax.perc)

        else:
            amount_taxable = \
                curr_tax.cap - tax_brackets[tax_idx-1].cap \
                if tax_idx != 0 \
                else curr_tax.cap
            after_tax = after_tax - (amount_taxable * curr_tax.perc)
            

def aggregate_taxes(adjusted_income, state_brackets, fed_brackets):
        final_result = adjusted_income

        if adjusted_income > 200000:
            final_result = (200000 * .9235) + ((adjusted_income - 200000) * .9145)
        else:
            final_result = final_result * (1 - 0.0765)
         

if __name__ == "__main__":
    federal_brackets = [
        TaxBracket(.1, 9700),
        TaxBracket(.12, 39475),
        TaxBracket(.22, 84200),
        TaxBracket(.24, 160725),
        TaxBracket(.32, 204100)
    ]

    # Interactive mode
    if len(sys.argv) > 1:
        if sys.argv[1] == '-i':
            while(True):
                income = float(input("Enter an income:"))
                print("Original:%.2f\tAfter Tax:%.2f " % (income, taxes_calc(income, federal_brackets)))
        else:
            incomes = list(map(int, sys.argv[1:]))
            print("Running calculations using ", incomes)
            
            for income in incomes:
                print("Original:%.2f\tAfter Tax:%.2f " % (income, taxes_calc(income, federal_brackets)))
        

    # Non-interactive mode
    else:
        incomes = [60000, 80000, 100000]
        interest_rates = [.04, .05, .06, .07, .08] 
        num_years = [6,7,8,9,10]


        # TESTING
        print("FEDERAL TAX TESTS")
        for income in incomes:
            print("Original:%.2f\tAfter Tax:%.2f " % (income, taxes_calc(income, federal_brackets)))
