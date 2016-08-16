num_items = int(input("Please enter the number of different items being purchased: "))

while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Please enter the number of different items being purchased: "))

quantities = []
costs = []
shipping_costs = []
total_item_cost = []

for i in range (1, (num_items + 1), 1):
    quantities.append(int(input("What is the quantity of item " + str(i) + ": ")))
    costs.append(float(input("What is the cost of item " + str(i) + ": $")))
    shipping_costs.append(float(input("What is the shipping cost of item " + str(i) + ": $")))

    total_item_cost.append(quantities[i-1] * costs[i - 1] + shipping_costs[i-1])

if sum(shipping_costs) > 100:
    total_cost = sum(total_item_cost) - 0.1 * sum(shipping_costs)
else:
    total_cost = sum(total_item_cost)

print("Total cost of order is: ${:.2f}".format(total_cost))



