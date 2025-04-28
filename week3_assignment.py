#calculating 20% of the price of an item if the discount is 20% or more
# This function calculates the final price after applying a discount if applicable.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(original_price, discount)

if final_price < original_price:
    print(f"The final price after discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${original_price:.2f}")
