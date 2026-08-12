# Define the product name as a string variable
product_name = "Wireless Mouse"

# Define the unit price of the product (in NPR)
unit_price = 1500

# Define the quantity of units sold
quantity_sold = 12

# Define the discount percentage as a decimal (10%)
discount_percentage = 0.10

# Calculate gross sales by multiplying price by quantity sold
gross_sales = unit_price * quantity_sold

# Calculate the discount amount based on gross sales and discount percentage
discount_amount = gross_sales * discount_percentage

# Calculate final sales by subtracting the discount from gross sales
final_sales = gross_sales - discount_amount

# Print the product name using an f-string
print(f"Product: {product_name}")

# Print the gross sales formatted to 2 decimal places
print(f"Gross sales: NPR {gross_sales:.2f}")

# Print the discount amount formatted to 2 decimal places
print(f"Discount: NPR {discount_amount:.2f}")

# Print the final sales amount formatted to 2 decimal places
print(f"Final sales: NPR {final_sales:.2f}")
