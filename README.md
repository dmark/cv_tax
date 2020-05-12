# Continuously Variable Income Tax

This is probably apocryphal, but one reason sometimes cited for simplifying income tax brackets is simplifying the calculations involved. I doubt this story but let's assume it was true at one time that the calculations involved were onerous. That is obviously no longer the case, as a few lines of code can be used to easily give every taxable dollar it's own tax rate.

This is in contrast to "chunky" progressive tax systems that have large cliffs at designated income levels.

Give every taxable dollar its own tax rate, where the tax rate on each dollar is calculated as:

    (max_tax_rate - min_tax_rate) / (top_taxable_dollar - bottom_taxable_dollar)

`bottom_taxable_dollar` is the nth dollar for which `min_tax_rate` applies, and `top_taxable_dollar` is the nth dollar for which `max_tax_rate` applies. All dollars above `top_taxable_dollar` are also taxed at `max_tax_rate`. So if:

1. your lowest tax rate is 0%,
1. your max tax rate is 90%,
1. your first $10,000 are tax free,
1. your max tax rate applies to your 250,000th dollar,
1. your income is $150,000

Then:

```
$ python3 cvt.py                                                                            
rate increment: 6.428571428571429e-06
62999.54999991482
```

Your income tax is $62,999.60.

Alternatively, instead of a linearly growing tax rate, you could probably use some kind of non-linear function to futher lower the tax burden on the lower end of your taxed dollars.

And with some pretty simple changes to the extremely naive code, you could have a negative `min_tax_rate`.
