def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount."""
    if discount_percent >= 20:  
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  


price = float(input("Enter the original price: $"))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if final_price == price:
    print(f"No discount applied. Final price: ${final_price:.2f}")
else:
    print(f"Discount applied! Final price after {discount_percent}% off: ${final_price:.2f}")
