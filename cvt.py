import argparse


def get_args():
    """Processes command line arguments"""
    parser = argparse.ArgumentParser(description='Continuously variable tax rate calculator.')
    parser.add_argument('-i', '--income')
    parser.add_argument('-r', '--rate_min', help='Minimum tax rate, as a decimal value')
    parser.add_argument('-R', '--rate_max', help='Maximum tax rate, as a decimal value')
    parser.add_argument('-d', '--dollar_min', help='Tax free dollars')
    parser.add_argument('-D', '--dollar_max', help='Income for max tax rate')
    return parser.parse_args()


def main():
    """main"""

    args = get_args()

    # if income > dollar_max then we apply the max rate to all dollars above
    # dollar_max
    max_rate_income = 0
    if int(args.income) > int(args.dollar_max):
        # rate_max is applied to all dollars above dollar_max
        max_rate_income = int(args.income) - int(args.dollar_max)
        # variable rate applies to dollars up to and including dollar_max
        variable_rate_income = int(args.dollar_max)
    else:
        variable_rate_income = int(args.income)

    # linearly increasing tax rate
    rate = float(args.rate_min)
    rate_increment = (float(args.rate_max) - float(args.rate_min)) / (int(args.dollar_max) - int(args.dollar_min))

    # calculate the fixed rate tax on dollars above dollar_max. May be zero.
    tax = max_rate_income * float(args.rate_max)
    # for every dollar between dollar_min and dollar_max, add the associated
    # tax.
    for dollar in range(0, variable_rate_income - int(args.dollar_min)):
        tax += rate
        rate += rate_increment

    print("tax:", round(tax), "|| marginal rate:", round(rate * 100), "|| average rate:",
          round(tax / int(args.income) * 100))

    # With list comprehensions - something is off about the calculations here
    # rate = float(args.rate_min)
    # tax_rate_per_dollar = [rate + rate_increment for dollar in range(0, variable_rate_income - int(args.dollar_min))]
    # dollars = [dollar for dollar in range(0, variable_rate_income - int(args.dollar_min))]
    # tax_per_dollar = [dollar * rate for dollar, rate in zip(dollars, tax_rate_per_dollar)]

    # print("tax:", round(sum(tax_per_dollar) + (max_rate_income * float(args.rate_max))), "|| marginal rate:",
    #       round(tax_per_dollar[-1] * 100), "|| average rate:", round(sum(tax_per_dollar) / variable_rate_income * 100))


if __name__ == '__main__':
    main()
