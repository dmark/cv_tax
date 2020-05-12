# cv_tax
Continuously Variable Tax Calculator

Give every taxable dollar its own tax rate, where the tax rate on each dollar is calculated as:

    (max_tax_rate - min_tax_rate) / taxable_dollars

This is in contrast to "chunky" progressive tax systems that have large cliffs at designated income levels.

Alternatively, each dollar up to some maximum has tax caluclated as above, and every dollar above the maximum is taxed at `max_tax_rate`.

Alternatively alternatively, instead of a linearly growing tax rate, you could probably use some kind of non-linear function to futher lower the tax burden on the less taxed dollars.
