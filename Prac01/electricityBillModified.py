TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Which Tariff? 11 or 31? "))
if tariff == 11:
    price = TARIFF_11 * 100
else:
    price = TARIFF_31 * 100

use = float(input("Please enter daily use in kWh: "))
billing_days = int(input("Please enter number of days in the billing period: "))

bill_cost = (billing_days * (use * price)) / 100
print("\nEstimated bill: ${:.2f}".format(bill_cost))