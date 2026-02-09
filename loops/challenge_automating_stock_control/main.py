# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item, stock in inventory.items():
	print(f"Processing {item}")	
	print(stock)
	stocks = inventory[item]
	while stocks[0] < stocks[1]:
		stocks[0] += stocks[2]
	for item in range(len(inventory)):
		if stocks[0] > discount_threshold:
			stocks[3] == True	
print("Processing completed")
print(inventory)