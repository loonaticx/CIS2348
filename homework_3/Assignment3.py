class ItemToPurchase:

    def __init__(self, item_name: str = "none", item_price: float = 0.0, item_quantity: int = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = int(self.item_quantity * self.item_price)
        return [f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${total_cost}", total_cost]


if __name__ == "__main__":
    itemData = []
    itemTotal = 0
    for i in range(1, 3):
        print(f"Item {i}")
        itemName = input("Enter the item name:\n")
        itemPrice = float(input("Enter the item price:\n"))
        itemQty = int(input("Enter the item quantity:\n"))
        print()
        item = ItemToPurchase(itemName, itemPrice, itemQty)
        itemData.append(item.print_item_cost())

    print("TOTAL COST")
    for item in itemData:
        print(item[0])
        itemTotal += item[1]
    print()
    print(f"Total: ${itemTotal}")
