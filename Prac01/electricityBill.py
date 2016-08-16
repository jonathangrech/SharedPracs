price = int(input("Please enter price of electricity supply in cents per kWh: "))
use = float(input("Please enter daily use in kWh: "))
billing_days = int(input("Please enter number of days in the billing period: "))

bill_cost = (billing_days * (use * price)) / 100
print("\nEstimated bill: ${:.2f}".format(bill_cost))