def calculate_total(price, quantity):
    return price * quantity
  # Function calculates total cost by multiplying price of item by the quantity of said item.

def calculate_change(payment, total):
    if payment >= total:
        return payment - total
    else:
        return total - payment
# Function calculates the change or the additional amount needed.

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))
# Asks user to enter the item price, quantity, and amount paid.

total_cost = calculate_total(item_price, quantity)
# Calls "calculate_total" function and gives calculated value to "total_cost"

amount = calculate_change(payment, total_cost)
# Calls "calculate_change" function and gives calculated value to "amount"

print(f"Total Cost: PHP {total_cost:.2f}")

if payment >= total_cost:
    print(f"Change: PHP {amount:.2f}")
else:
    print(f"Additional amount needed: PHP {amount:.2f}")
# Displays the total cost and the change or shortage.
  
