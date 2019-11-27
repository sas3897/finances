"""

"""
from TaxBrackets import *

FED_STD_DEDUCTION = 12200
STARTING_AGE = 22


def taxes_calc(taxable_income, tax_brackets):
    """
    Calculates and returns the post-tax amount given the taxable income, and the relevant tax brackets.
    This function assumes that your income is below the cap of at least one tax bracket in tax_brackets,
    as this is how all tax_brackets I know of work.
    """

    after_tax = taxable_income

    for tax_idx in range(0, len(tax_brackets)):
        curr_tax = tax_brackets[tax_idx]

        if taxable_income < curr_tax.cap:
            return after_tax - ((taxable_income - tax_brackets[tax_idx - 1].cap) * curr_tax.perc)

        else:
            amount_taxable = curr_tax.cap - tax_brackets[tax_idx-1].cap \
                if tax_idx != 0 \
                else curr_tax.cap
            after_tax = after_tax - (amount_taxable * curr_tax.perc)


def fica(gross_income):
    """
    Calculates and returns the money one has post-FICA deductions, assuming one
    is an employee and thus only pays half the FICA tax.
    """
    # FICA, with additional tax on income over 200,000
    if gross_income > 200000:
        return (200000 * .9235) + ((gross_income - 200000) * .9145)
    else:
        return gross_income * (1 - 0.0765)


# TODO These are just the tip of the iceberg, applying to an idealized homogeneous 'income'
# TODO instead of being split up into asset classes, with an asset distribution you'll be
# TODO holding onto, etc.
def compound_interest(years, gross_income, interest, income_growth, fed_brackets, state_brackets, local_brackets, fed_deduct, state_deduct, local_deduct):
    final_wealth = 0
    for year in range(years):
        growth = final_wealth * interest  # Growth due to interest

        # Added wealth is post-tax combination of "gross_income" (wage income) and interest on assets
        final_wealth += standard_deduction(gross_income + growth, fed_brackets, state_brackets,
                                           local_brackets, fed_deduct, state_deduct, local_deduct)
        # Yearly wage growth
        gross_income *= (1 + income_growth)

    return final_wealth


def standard_deduction(gross_income, fed_brackets, state_brackets, local_brackets,
                       fed_deduct, state_deduct, local_deduct):
    final_result = fica(gross_income)

    fed_losses = 0 if gross_income < fed_deduct \
        else (gross_income - fed_deduct) - taxes_calc(gross_income - fed_deduct, fed_brackets)

    state_losses = 0 if gross_income < state_deduct \
        else (gross_income - state_deduct) - taxes_calc(gross_income - state_deduct, state_brackets)

    local_losses = 0 if gross_income < local_deduct \
        else (gross_income - local_deduct) - taxes_calc(gross_income - local_deduct, local_brackets)

    return final_result - (fed_losses + state_losses + local_losses)


def main():
    # Command-line invocation
    if len(sys.argv) > 1:
        # Interactive mode
        if sys.argv[1] == '-i':
            while True:
                income = float(input("Enter an income:"))
                print("Original:%.2f\tAfter Tax:%.2f " %
                      (income, standard_deduction(income, federal_brackets_single, md_brackets_single,
                                                  moco_bracket, FED_STD_DEDUCTION, 0, 0)))
        else:
            incomes = list(map(int, sys.argv[1:]))
            print("Running calculations using ", incomes)

            for income in incomes:
                print("Original:%.2f\tAfter Tax:%.2f "
                      % (income,
                         standard_deduction(income, federal_brackets_single, md_brackets_single,
                                            moco_bracket, FED_STD_DEDUCTION, 0, 0)))

    # Non-interactive mode
    else:
        incomes = [9700, 60000, 78000, 100000]
        interest_rates = [.04, .05, .06, .07, .08]
        num_years = [6, 7, 8, 9, 10]

        # TESTING
        print("\nUSING STANDARD DEDUCTION")
        for income in incomes:
            post_tax = standard_deduction(income, federal_brackets_single, md_brackets_single, moco_bracket, FED_STD_DEDUCTION, 0, 0)
            print("Original:%.2f\tAfter Tax:%.2f\tTax Burden:%.2f " % (income, post_tax, income - post_tax))

        print("\nCOMPOUND GROWTH")
        for year in num_years:
            print("\nOver %d years..." % year)
            first_entry = True
            for interest in interest_rates:
                if first_entry:
                    first_entry = False
                else:
                    print("")
                print("With %.2f interest rate..." % interest)
                for income in incomes:
                    print("Starting Income: %.2f\tFinal wealth: %.2f"
                          % (income, compound_interest(year, income, interest, .03, federal_brackets_single,
                                                       md_brackets_single, moco_bracket, FED_STD_DEDUCTION, 0, 0)))

if __name__ == "__main__":
    main()