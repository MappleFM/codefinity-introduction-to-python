# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for item in products:
	product = item
	price, quantity_sold = products[item]
	print(f"{item} has price {price} and q sold {quantity_sold}")
	priceF = float(price)
	quantity_soldI = int(quantity_sold)
	total_sales = priceF * quantity_soldI
	print(f"Total sales for {product}: ${total_sales}")
	total_sales_list.append(total_sales)
print(total_sales_list)
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")