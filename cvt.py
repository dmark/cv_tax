rate_min = 0.0
rate_max = 0.9
dollar_min = 10000
dollar_max = 250000

income = 150000
tax = 0.0

rate_increment = (rate_max - rate_min) / (income - dollar_min)
rate = rate_min

print("rate increment:", rate_increment)

for dollar in range(0, income - dollar_min):
    tax += rate
    rate += rate_increment

print(tax)
