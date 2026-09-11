inventory = 0
rejected_input = 0

while True:
    stock_quantity = input("Enter a stock quantity, or 'quit' to quit: ").strip()

    if stock_quantity.lower() == "quit":
        print(f"Total Units Processed: {inventory}")
        print(f"Number of Rejected Entries: {rejected_input}")
        break

    if stock_quantity.startswith("-"):
        print("Error: Input is negative!")
        rejected_input += 1
        continue

    if stock_quantity == "" or not stock_quantity.isdigit():
        print("Error: Input must be a whole number!")
        rejected_input += 1
        continue

    inventory += int(stock_quantity)

    if inventory > 500:
        print(f"Error: Total inventory is overstocked! (total = {inventory})")
        break
    else:
        print(f"Okay: Total inventory is now {inventory}.")
